function handleContact(e){
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target).entries());
  alert(`Thanks, ${data.name}! We'll be in touch at ${data.email}.`);
}
// FAQ accordion
document.addEventListener('click', (e)=>{
  if(e.target.classList.contains('faq-q')){
    const ans = e.target.nextElementSibling;
    const open = ans.style.display === 'block';
    document.querySelectorAll('.faq .faq-a').forEach(a=>a.style.display='none');
    ans.style.display = open ? 'none' : 'block';
  }
});
