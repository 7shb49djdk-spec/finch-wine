/* Offline support. Bump VERSION whenever any file changes (tools/build_data.py does it for data updates),
   so phones fetch the new list and offer to reload. */
var VERSION = 'finch-2026-11-06-7a55fa4e';
var FILES = [
  './', 'index.html', 'css/app.css', 'js/app.js', 'js/data.js', 'manifest.webmanifest',
  'fonts/Poppins-Light.ttf', 'fonts/Poppins-LightItalic.ttf', 'fonts/Poppins-Medium.ttf',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png'
];

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(VERSION).then(function (c) { return c.addAll(FILES); }));
});
self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== VERSION; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener('message', function (e) { if (e.data === 'skipWaiting') self.skipWaiting(); });
self.addEventListener('fetch', function (e) {
  if (e.request.method !== 'GET') return;
  e.respondWith(caches.match(e.request, { ignoreSearch: true }).then(function (hit) {
    return hit || fetch(e.request).catch(function () { return caches.match('index.html'); });
  }));
});
