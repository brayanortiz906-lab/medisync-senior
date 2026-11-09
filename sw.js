// Service Worker para MediSync Senior (modo offline)
const CACHE_NAME = 'medisync-v1';
const ASSETS = [
  './',
  './prototipo_funcional.html',
  './prototipo_simple.html',
  './landing_medisync_senior.html',
  './index.html',
  './styles.css',
  './assets/fontawesome/all.min.css',
  './assets/fontawesome/webfonts/fa-solid-900.woff2',
  './assets/fontawesome/webfonts/fa-regular-400.woff2',
  './assets/fontawesome/webfonts/fa-brands-400.woff2',
  './img/caja_paracetamol.png',
  './img/pastillas.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS)).catch(()=>{})
  );
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter(k=>k!==CACHE_NAME).map(k=>caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;
  e.respondWith(
    caches.match(req).then((cached) => {
      const fetchPromise = fetch(req).then((res) => {
        if (res && res.status === 200) {
          const clone = res.clone();
          caches.open(CACHE_NAME).then((c) => c.put(req, clone));
        }
        return res;
      }).catch(() => cached);
      return cached || fetchPromise;
    })
  );
});
