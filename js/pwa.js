/* Application installable : service worker + bouton « Installer ». */
(function () {
  "use strict";

  // Le service worker n'existe qu'en http(s) (pas en ouvrant le fichier depuis le disque).
  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("sw.js").catch((err) => console.warn("Service worker :", err));
    });
  }

  const bouton = document.getElementById("installer");
  if (!bouton) return;

  let invite = null;
  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    invite = e;
    bouton.hidden = false;
  });

  bouton.addEventListener("click", async () => {
    if (!invite) return;
    bouton.hidden = true;
    invite.prompt();
    await invite.userChoice;
    invite = null;
  });

  window.addEventListener("appinstalled", () => {
    bouton.hidden = true;
  });
})();
