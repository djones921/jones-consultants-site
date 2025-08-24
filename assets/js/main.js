// FAQ toggle
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const answer = btn.nextElementSibling;
    answer.style.display = answer.style.display === 'block' ? 'none' : 'block';
  });
});

// Smooth scroll on nav clicks
document.querySelectorAll("nav a[href^='#']").forEach(link => {
  link.addEventListener("click", e => {
    e.preventDefault();
    const targetId = link.getAttribute("href").slice(1);
    const targetEl = document.getElementById(targetId);
    if (targetEl) {
      targetEl.scrollIntoView({ behavior: "smooth" });
    }
  });
});

// Scrollspy
document.addEventListener("DOMContentLoaded", () => {
  const sections = document.querySelectorAll("main > section[id]");
  const navLinks = document.querySelectorAll("nav a[href^='#']");

  function setActiveLink() {
    let currentSection = "hero"; // fallback to hero at very top
    const scrollY = window.scrollY;
    const offset = 80; // adjust for sticky header

    sections.forEach(section => {
      const sectionTop = section.offsetTop - offset;
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        currentSection = section.id;
      }
    });

    navLinks.forEach(link => {
      link.classList.toggle(
        "active",
        link.getAttribute("href") === `#${currentSection}`
      );
    });
  }

  window.addEventListener("scroll", setActiveLink);
  setActiveLink(); // run once on load
});
