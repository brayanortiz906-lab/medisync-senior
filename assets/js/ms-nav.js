(function () {
  var nav = document.getElementById('msnNav');
  if (!nav) return;

  var sysBtn = document.getElementById('msnSysBtn');
  var sysMenu = document.getElementById('msnSysMenu');
  var burger = document.getElementById('msnBurger');
  var mobile = document.getElementById('msnMobile');

  function onScroll() {
    nav.classList.toggle('is-scrolled', window.scrollY > 20);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  function closeSys() {
    if (!sysMenu || !sysBtn) return;
    sysMenu.classList.remove('open');
    sysBtn.setAttribute('aria-expanded', 'false');
  }

  function closeMobile() {
    if (!mobile || !burger) return;
    mobile.classList.remove('open');
    burger.setAttribute('aria-expanded', 'false');
    var icon = burger.querySelector('i');
    if (icon) {
      icon.classList.add('fa-bars');
      icon.classList.remove('fa-xmark');
    }
  }

  if (sysBtn && sysMenu) {
    sysBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = sysMenu.classList.toggle('open');
      sysBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('click', function (e) {
      if (!sysMenu.contains(e.target) && !sysBtn.contains(e.target)) closeSys();
    });
  }

  if (burger && mobile) {
    burger.addEventListener('click', function (e) {
      e.stopPropagation();
      var open = mobile.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      var icon = burger.querySelector('i');
      if (icon) {
        icon.classList.toggle('fa-bars', !open);
        icon.classList.toggle('fa-xmark', open);
      }
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      closeSys();
      closeMobile();
    }
  });

  if (mobile) {
    mobile.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMobile);
    });
  }
})();
