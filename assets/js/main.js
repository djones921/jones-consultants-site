// FAQ toggle
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const answer = btn.nextElementSibling;
    answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
  });
});

// Scrollspy + smooth scroll
document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll("main > section[id]");
  const navLinks = document.querySelectorAll("nav a[href^='#']");

  // Highlight active nav link
  function setActiveLink() {
    let currentSection = "";
    const midpoint = window.scrollY + window.innerHeight / 2;

    sections.forEach(section => {
      const top = section.offsetTop;
      const bottom = top + section.offsetHeight;
      if (midpoint >= top && midpoint <= bottom) {
        currentSection = section.id;
      }
    });

    navLinks.forEach(link => {
      link.classList.toggle("active", link.getAttribute("href") === `#${currentSection}`);
    });
  }

  // Smooth scroll on click
  navLinks.forEach(link => {
    link.addEventListener("click", e => {
      e.preventDefault();
      const targetId = link.getAttribute("href").slice(1);
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

  window.addEventListener("scroll", setActiveLink);
  setActiveLink(); // run once on load
});