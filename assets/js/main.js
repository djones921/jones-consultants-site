// Smooth FAQ toggle
document.querySelectorAll('.faq-q').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    const a=btn.nextElementSibling;
    a.style.display = a.style.display==='block' ? 'none' : 'block';
  });
});

// Scrollspy for nav links
const sections = document.querySelectorAll('main > section[id]');
const navLinks = document.querySelectorAll('nav a[href^="#"]');

function activateLink() {
  let index = sections.length;

  while(--index && window.scrollY + 60 < sections[index].offsetTop) {}
  
  navLinks.forEach((link) => link.classList.remove('active'));
  if(navLinks[index]) navLinks[index].classList.add('active');
}

activateLink();
window.addEventListener('scroll', activateLink);
