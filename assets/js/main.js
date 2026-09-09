/* JCS Engineering site behaviour */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Current year -------------------------------------------------------- */
  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  /* Mobile navigation --------------------------------------------------- */
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('primary-nav');

  function setNav(open) {
    if (!toggle || !nav) return;
    nav.classList.toggle('open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setNav(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setNav(false);
        toggle.focus();
      }
    });
    document.addEventListener('click', function (e) {
      if (toggle.getAttribute('aria-expanded') !== 'true') return;
      if (!nav.contains(e.target) && !toggle.contains(e.target)) setNav(false);
    });
    window.addEventListener('resize', function () {
      if (window.innerWidth > 820) setNav(false);
    });
  }

  /* Header shadow on scroll --------------------------------------------- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () { header.classList.toggle('scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* FAQ accordion (single-open) ----------------------------------------- */
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    var panel = btn.parentElement.nextElementSibling;
    if (!panel) return;
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.faq-q[aria-expanded="true"]').forEach(function (other) {
        if (other === btn) return;
        other.setAttribute('aria-expanded', 'false');
        var op = other.parentElement.nextElementSibling;
        if (op) op.hidden = true;
      });
      btn.setAttribute('aria-expanded', String(!open));
      panel.hidden = open;
    });
  });

  /* Reveal on scroll ---------------------------------------------------- */
  var revealables = document.querySelectorAll('.reveal');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealables.forEach(function (el) { el.classList.add('in'); });
  } else {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('in');
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    revealables.forEach(function (el) {
      // Stagger siblings so grids cascade instead of popping in together.
      var i = Array.prototype.indexOf.call(el.parentElement.children, el);
      el.style.transitionDelay = Math.min(i, 5) * 60 + 'ms';
      revealObserver.observe(el);
    });
  }

  /* Deep links into the capabilities page ------------------------------- */
  // Anchored capability blocks are revealed on load so a #hash landing isn't blank.
  if (location.hash) {
    var target = document.querySelector(location.hash);
    if (target) target.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }

  /* Contact form: submit inline, show a thank-you state ----------------- */
  var form = document.getElementById('contact-form');
  if (form && window.fetch && window.FormData) {
    var status = document.getElementById('form-status');
    var submit = form.querySelector('button[type="submit"]');
    var successTpl = document.getElementById('form-success-tpl');

    function showError(msg) {
      status.hidden = false;
      status.className = 'form-status err';
      status.textContent = msg;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Native validation first, with the browser's own messaging.
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      status.hidden = true;
      submit.disabled = true;
      var label = submit.innerHTML;
      submit.textContent = 'Sending…';

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function (res) {
        if (!res.ok) throw new Error('HTTP ' + res.status);
        return res.json();
      }).then(function () {
        if (successTpl) {
          form.replaceWith(successTpl.content.cloneNode(true));
        } else {
          form.reset();
          status.hidden = false;
          status.className = 'form-status';
          status.textContent = 'Message received. We’ll be in touch within one business day.';
        }
        // Move focus so screen readers announce the outcome.
        var h = document.querySelector('.form-success h3');
        if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
      }).catch(function () {
        submit.disabled = false;
        submit.innerHTML = label;
        showError('Something went wrong sending your message. Please try again, or email drew@jcseng.com directly.');
      });
    });
  }
})();
