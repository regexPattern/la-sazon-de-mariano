(async () => {
  const jsConfetti = new JSConfetti()
  jsConfetti.addConfetti()
  await (new Promise((resolve) => setTimeout(resolve, 2000)));
  window.location.replace("/signin")
})();
