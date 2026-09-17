const navToggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.site-nav');

if (navToggle && nav) {
  navToggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const reveals = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.12,
  }
);

reveals.forEach((element) => revealObserver.observe(element));

const contactForm = document.querySelector('.contact-form');

if (contactForm) {
  contactForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const submitButton = contactForm.querySelector('button[type="submit"]');
    if (submitButton) {
      submitButton.textContent = 'MESSAGE SENT';
      submitButton.disabled = true;
    }
  });
}
