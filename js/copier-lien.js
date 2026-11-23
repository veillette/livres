// Une adresse relative conserve le sous-dossier du site.
document.addEventListener("click", async (evenement) => {
  const bouton = evenement.target.closest?.("button[data-copy-link]");
  if (!bouton) return;

  const adresse = new URL(bouton.dataset.copyLink, location.href).href;
  const message = bouton.nextElementSibling;
  try {
    await navigator.clipboard.writeText(adresse);
  } catch {
    window.prompt("Copiez ce lien :", adresse);
    return;
  }

  message.textContent = "Lien copié.";
});
