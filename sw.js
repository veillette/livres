/*
 * Service worker : rend le site utilisable hors ligne.
 *
 * À l'installation, on met en cache l'interface puis TOUS les livres du
 * catalogue : on lit `livres/catalogue.js`, puis chaque `livre.js` pour y
 * trouver les images.
 *
 * L'installation n'a lieu que quand ce fichier change : après l'ajout d'un
 * livre ou la modification d'images, augmenter VERSION pour que tout soit
 * de nouveau téléchargé et disponible hors ligne. Les fichiers inchangés
 * sont revalidés auprès du serveur (réponse 304), pas re-téléchargés.
 *
 * Stratégies :
 *  - pages, scripts, styles : réseau d'abord (pour voir les nouveautés),
 *    cache si hors ligne ;
 *  - images et polices : cache seulement, sans requête réseau quand elles y
 *    sont déjà (elles ne changent qu'avec VERSION) ;
 *  - sur localhost : toujours le réseau d'abord, pour voir tout de suite les
 *    images régénérées pendant qu'on dessine.
 */
const VERSION = "v21";
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
  "polices/andika-400.woff2",
  "polices/andika-700.woff2",
  "polices/fredoka.woff2",
];

const EN_LOCAL = ["localhost", "127.0.0.1", "[::1]"].includes(self.location.hostname);

/* Requête qui revalide le cache HTTP du navigateur (If-None-Match) : un
   fichier inchangé coûte une réponse 304 au lieu d'un nouveau téléchargement. */
const revalider = (url) => new Request(url, { cache: "no-cache" });

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
      await cache.addAll(INTERFACE.map(revalider));
      const livres = await fichiersDesLivres().catch(() => []);
      // Un fichier manquant ne doit pas faire échouer toute l'installation.
      await Promise.all(livres.map((url) => cache.add(revalider(url)).catch(() => null)));
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

/* Pour les pages, la clé de cache ignore les paramètres : lire.html?livre=a
   et lire.html?livre=b partagent une seule entrée « lire.html ». */
function cleDeCache(requete) {
  if (requete.mode !== "navigate") return requete;
  const url = new URL(requete.url);
  return url.origin + url.pathname;
}

async function reseauDAbord(requete) {
  const cache = await caches.open(CACHE);
  try {
    const reponse = await fetch(requete);
    if (reponse.ok) await cache.put(cleDeCache(requete), reponse.clone());
    return reponse;
  } catch (err) {
    const enCache = await cache.match(cleDeCache(requete), { ignoreSearch: requete.mode === "navigate" });
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
  if (enCache) return enCache;
  const reponse = await fetch(requete);
  if (reponse.ok) await cache.put(requete, reponse.clone());
  return reponse;
}

self.addEventListener("fetch", (event) => {
  const requete = event.request;
  if (requete.method !== "GET") return;
  const url = new URL(requete.url);
  if (url.origin !== self.location.origin) return;

  if (!EN_LOCAL && /\.(svg|png|jpe?g|webp|gif|woff2)$/i.test(url.pathname)) {
    event.respondWith(cacheDAbord(requete));
  } else {
    event.respondWith(reseauDAbord(requete));
  }
});
