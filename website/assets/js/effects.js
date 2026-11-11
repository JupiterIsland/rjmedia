(function () {
  'use strict';

  // Respect motion preferences
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Cursor spotlight (dark pages only) ----------
  if (!reduceMotion && document.body.classList.contains('theme-community')) {
    var raf = null;
    document.addEventListener('pointermove', function (e) {
      if (raf) return;
      raf = requestAnimationFrame(function () {
        document.documentElement.style.setProperty('--cursor-x', e.clientX + 'px');
        document.documentElement.style.setProperty('--cursor-y', e.clientY + 'px');
        raf = null;
      });
    }, { passive: true });
  }

  // ---------- Scroll reveal fallback ----------
  // Only fires if the browser lacks native scroll-timeline.
  var supportsScrollTimeline = CSS.supports && CSS.supports('animation-timeline: view()');

  if (!supportsScrollTimeline && !reduceMotion) {
    document.documentElement.classList.add('no-scroll-timeline');

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.reveal').forEach(function (el) {
      observer.observe(el);
    });
  }
})();
