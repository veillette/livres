/*
 * Service worker : rend le site utilisable hors ligne.
 *
 * À l'installation, on met en cache l'interface puis TOUS les livres du
 * catalogue : on lit `livres/catalogue.js`, puis chaque `livre.js` pour y
 * trouver les images. Ajouter un livre ne demande donc rien de plus ici.
 *
 * Stratégies :
 *  - pages, scripts, styles : réseau d'abord (pour voir les nouveautés),
 *    cache si hors ligne ;
 *  - images et polices : cache d'abord, mis à jour en arrière-plan.
 *
 * Changer VERSION force le renouvellement complet du cache.
 */
const VERSION = "v6";
const CACHE = `livres-${VERSION}`;

const INTERFACE = [
  "./",
  "index.html",
  "lire.html",
  "imprimer.html",
  "manifest.webmanifest",
  "css/site.css",
  "css/pages.css",
  "js/livres.js",
  "js/bibliotheque.js",
  "js/lecteur.js",
  "js/imposition.js",
  "js/impression.js",
  "js/pwa.js",
  "livres/catalogue.js",
  "icones/icone.svg",
  "icones/icone-192.png",
  "icones/icone-512.png",
  "icones/icone-masquable-512.png",
  "icones/apple-touch-icon.png",
];

async function fichiersDesLivres() {
  const reponse = await fetch("livres/catalogue.js", { cache: "no-cache" });
  const texte = await reponse.text();
  const liste = texte.match(/CATALOGUE\s*=\s*\[([\s\S]*?)\]/);
  const ids = liste ? [...liste[1].matchAll(/["']([a-z0-9-]+)["']/g)].map((m) => m[1]) : [];

  const fichiers = [];
  await Promise.all(
    ids.map(async (id) => {
      const dossier = `livres/${id}/`;
      fichiers.push(`${dossier}livre.js`);
      try {
        const source = await (await fetch(`${dossier}livre.js`, { cache: "no-cache" })).text();
        for (const m of source.matchAll(/["'](images\/[^"']+)["']/g)) fichiers.push(dossier + m[1]);
      } catch {
        /* livre introuvable : on l'ignore */
      }
    })
  );
  return [...new Set(fichiers)];
}

self.addEventListener("install", (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(CACHE);
      await cache.addAll(INTERFACE);
      const livres = await fichiersDesLivres().catch(() => []);
      // Un fichier manquant ne doit pas faire échouer toute l'installation.
      await Promise.all(livres.map((url) => cache.add(url).catch(() => null)));
      await self.skipWaiting();
    })()
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    (async () => {
      const noms = await caches.keys();
      await Promise.all(noms.filter((n) => n.startsWith("livres-") && n !== CACHE).map((n) => caches.delete(n)));
      await self.clients.claim();
    })()
  );
});

async function reseauDAbord(requete, options) {
  const cache = await caches.open(CACHE);
  try {
    const reponse = await fetch(requete);
    if (reponse.ok) cache.put(requete, reponse.clone());
    return reponse;
  } catch (err) {
    const enCache = await cache.match(requete, options);
    if (enCache) return enCache;
    if (requete.mode === "navigate") {
      const accueil = await cache.match("index.html");
      if (accueil) return accueil;
    }
    throw err;
  }
}

async function cacheDAbord(requete) {
  const cache = await caches.open(CACHE);
  const enCache = await cache.match(requete);
  const miseAJour = fetch(requete)
    .then((reponse) => {
      if (reponse.ok || reponse.type === "opaque") cache.put(requete, reponse.clone());
      return reponse;
    })
    .catch(() => null);
  return enCache || (await miseAJour) || Response.error();
}

self.addEventListener("fetch", (event) => {
  const requete = event.request;
  if (requete.method !== "GET") return;
  const url = new URL(requete.url);

  // Polices Google : cache d'abord.
  if (url.hostname === "fonts.googleapis.com" || url.hostname === "fonts.gstatic.com") {
    event.respondWith(cacheDAbord(requete));
    return;
  }
  if (url.origin !== self.location.origin) return;

  if (requete.mode === "navigate") {
    // lire.html?livre=… : on sert lire.html depuis le cache, quel que soit le paramètre.
    event.respondWith(reseauDAbord(requete, { ignoreSearch: true }));
  } else if (/\.(svg|png|jpe?g|webp|gif)$/i.test(url.pathname)) {
    event.respondWith(cacheDAbord(requete));
  } else {
    event.respondWith(reseauDAbord(requete));
  }
});
