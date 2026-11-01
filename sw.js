const CACHE='practicals-ai-shell-v4';
const ASSETS=['./','./index.html','./manifest.webmanifest'];
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)));self.skipWaiting()});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k!==CACHE).map(k=>caches.delete(k)))));self.clients.claim()});
self.addEventListener('fetch',event=>{
 const req=event.request,url=new URL(req.url);
 if(req.method!=='GET'||url.origin!==location.origin)return;
 if(req.mode==='navigate'){
  event.respondWith(fetch(req).then(res=>{if(res.ok)caches.open(CACHE).then(c=>c.put('./',res.clone()));return res}).catch(()=>caches.match('./').then(cached=>cached||caches.match('./index.html'))));
  return;
 }
 event.respondWith(caches.match(req).then(cached=>{
  const network=fetch(req).then(res=>{if(res.ok)caches.open(CACHE).then(c=>c.put(req,res.clone()));return res});
  return cached||network.catch(()=>caches.match('./index.html'));
 }));
});