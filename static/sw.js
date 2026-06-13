// Simple Service Worker for PWA
self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open('sw-toolkit-cache').then((cache) => cache.addAll([
      '/',
      '/static/manifest.json'
    ])),
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((response) => response || fetch(e.request)),
  );
});
