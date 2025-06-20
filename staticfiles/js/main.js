document.addEventListener('DOMContentLoaded', () => {
  const html = document.documentElement;
  const darkToggle = document.getElementById('darkToggle');
  const mobileToggle = document.getElementById('mobile-dark-toggle');
  const moonIcon = document.getElementById('moon');
  const sunIcon = document.getElementById('sun');

  // Apply stored preference
  const theme = localStorage.theme;
  if (theme === 'dark') {
    html.classList.add('dark');
    moonIcon.classList.add('hidden');
    sunIcon.classList.remove('hidden');
  } else {
    html.classList.remove('dark');
    moonIcon.classList.remove('hidden');
    sunIcon.classList.add('hidden');
  }

  function toggleTheme() {
    const isDark = html.classList.contains('dark');
    html.classList.toggle('dark');
    localStorage.theme = isDark ? 'light' : 'dark';

    moonIcon.classList.toggle('hidden');
    sunIcon.classList.toggle('hidden');
  }

  if (darkToggle) darkToggle.addEventListener('click', toggleTheme);
  if (mobileToggle) mobileToggle.addEventListener('click', toggleTheme);
});
