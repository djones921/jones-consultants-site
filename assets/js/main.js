// assets/js/main.js

// FAQ toggle
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const a = btn.nextElementSibling;
    a.style.display = a.style.display === 'block' ? 'none' : 'block';
  });
});

// Smooth scroll for in-page links
document.querySelectorAll('nav a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const targetId = link.getAttribute('href').slice(1);
    const targetEl = document.getElementById(targetId);
    if (!targetEl) return;
    e.preventDefault();

    // account for sticky header height
    const headerOffset = document.querySelector('.site-header').offsetHeight;
    const elementPosition = targetEl.getBoundingClientRect().top + window.scrollY;
    const offsetPosition = elementPosition - headerOffset + 5;

    window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
  });
});

// Scrollspy using IntersectionObserver
document.addEventListener('DOMContentLoaded', () => {
  const navLinks = Array.from(document.querySelectorAll('nav a[href^="#"]'));
  const sections = navLinks
    .map(l => document.querySelector(l.getAttribute('href')))
    .filter(Boolean);

  // Helper to set active link
  const setActive = (id) => {
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
    });
  };

  const headerHeight = document.querySelector('.site-header').offsetHeight;

  const observer = new IntersectionObserver((entries) => {
    const visible = entries
      .filter(e => e.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible) setActive(visible.target.id);
  }, {
    root: null,
    rootMargin: `-${headerHeight + 20}px 0px -60% 0px`, // shift trigger down to account for sticky header
    threshold: [0.2, 0.4, 0.6, 0.8]
  });

  sections.forEach(sec => observer.observe(sec));

  // Ensure "Home" is active at the very top
  if (window.scrollY < 10) setActive('hero');
});
