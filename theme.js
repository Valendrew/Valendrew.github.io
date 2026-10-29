(() => {
  const preference = window.matchMedia('(prefers-color-scheme: dark)');
  let saved;
  try { saved = localStorage.getItem('portfolio-theme'); } catch {}
  if (saved === 'light' || saved === 'dark') document.documentElement.dataset.theme = saved;
  const isDark = () => document.documentElement.dataset.theme
    ? document.documentElement.dataset.theme === 'dark' : preference.matches;
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.querySelector('.theme-toggle');
    const update = () => button.setAttribute('aria-pressed', String(isDark()));
    button.hidden = false;
    update();
    preference.addEventListener('change', update);
    button.addEventListener('click', () => {
      const theme = isDark() ? 'light' : 'dark';
      document.documentElement.dataset.theme = theme;
      try { localStorage.setItem('portfolio-theme', theme); } catch {}
      update();
    });
  });
})();
