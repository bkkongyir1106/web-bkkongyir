// Use native anchor scrolling instead of the legacy theme's html/body animation.
// Capture only links to actual sections on this page; other links keep their
// ordinary browser behavior (including the publication archive's filter hashes).
document.addEventListener('click', function (event) {
  const link = event.target.closest('a[href]');
  if (!link || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const url = new URL(link.href, window.location.href);
  if (url.origin !== location.origin || url.pathname !== location.pathname || !url.hash) return;
  const section = document.getElementById(decodeURIComponent(url.hash.slice(1)));
  if (!section || !section.classList.contains('home-section')) return;
  event.preventDefault();
  event.stopPropagation();
  const menu = document.getElementById('navbar-content');
  const toggle = document.querySelector('.navbar-toggler');
  if (menu) menu.classList.remove('show');
  if (toggle) toggle.setAttribute('aria-expanded', 'false');
  history.pushState(null, '', url.hash);
  const heading = section.querySelector('h1, h2');
  if (heading) {
    heading.setAttribute('tabindex', '-1');
    heading.focus({preventScroll: true});
  }
  section.scrollIntoView({behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start'});
}, true);
