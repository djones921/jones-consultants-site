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
    targetEl.scrollIntoView({ behavior: 'smooth' });
  });
});

// Scrollspy using IntersectionObserver (works on mobile & desktop)
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

  // Observe section visibility around viewport center-ish
  const observer = new IntersectionObserver((entries) => {
    // Pick the most visible entry
    const visible = entries
      .filter(e => e.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible) setActive(visible.target.id);
  }, {
    root: null,
    // This focuses detection to the middle band of the screen,
    // making the highlight feel natural while scrolling.
    rootMargin: '-35% 0px -55% 0px',
    threshold: [0.1, 0.25, 0.5, 0.75]
  });

  sections.forEach(sec => observer.observe(sec));

  // Ensure "Home" is active at the very top
  if (window.scrollY < 10) setActive('hero');
});
