/* Bara demo + watermark pentru temele de pe stomatologie.devhub.md */
(function () {
  var STORE = 'https://stan.store/devhubmd';
  var THEMES = [
    { id: 'lumen', name: 'Lumen', buy: STORE + '/p/site-pentru-clinic-stomatologic--lumen', tag: { ro: 'Clinică', en: 'Clinic', ru: 'Клиника', it: 'Studio', uk: 'Клініка' } },
    { id: 'smile', name: 'Smile Line', buy: STORE + '/p/site-ortodontie-smile-line', tag: { ro: 'Ortodonție', en: 'Orthodontics', ru: 'Ортодонтия', it: 'Ortodonzia', uk: 'Ортодонтія' } }
  ];
  var T = {
    ro: { all: 'Toate design-urile', demo: 'Demo', admin: 'Panoul de administrare', buy: 'Cumpără acest site · 99 €', buyShort: '99 €', turnkey: 'La cheie de la 300 €', nav: 'Alte design-uri demo' },
    en: { all: 'All designs', demo: 'Demo', admin: 'Admin panel', buy: 'Buy this website · €99', buyShort: '€99', turnkey: 'Done for you from €300', nav: 'Other demo designs' },
    ru: { all: 'Все дизайны', demo: 'Демо', admin: 'Панель управления', buy: 'Купить этот сайт · 99 €', buyShort: '99 €', turnkey: 'Под ключ от 300 €', nav: 'Другие демо-дизайны' },
    it: { all: 'Tutti i design', demo: 'Demo', admin: 'Pannello di gestione', buy: 'Acquista questo sito · 99 €', buyShort: '99 €', turnkey: 'Chiavi in mano da 300 €', nav: 'Altri design demo' },
    uk: { all: 'Усі дизайни', demo: 'Демо', admin: 'Панель керування', buy: 'Купити цей сайт · 99 €', buyShort: '99 €', turnkey: 'Під ключ від 300 €', nav: 'Інші демо-дизайни' }
  };
  var parts = location.pathname.split('/').filter(Boolean);
  var cur = parts[0];
  var lang = T[parts[1]] ? parts[1] : 'ro';
  var sub = lang === 'ro' ? '' : lang + '/';
  var home = '/' + sub;
  var t = T[lang];
  var theme = THEMES.filter(function (x) { return x.id === cur; })[0] || THEMES[0];
  var H = 44;

  var css =
    ':root{--demo-h:' + H + 'px}html{scroll-padding-top:calc(' + H + 'px + 84px)!important}' +
    '.dk-bar{position:sticky;top:0;z-index:2147483000;height:' + H + 'px;display:flex;align-items:center;gap:10px;padding:0 12px;background:#0f1a1a;color:#f4f4f5;font:500 13px/1 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;border-bottom:1px solid #22302f;box-sizing:border-box}' +
    '.dk-bar *{box-sizing:border-box}.dk-bar a{color:inherit;text-decoration:none}' +
    '.dk-home{display:inline-flex;align-items:center;gap:8px;white-space:nowrap;padding:6px 10px 6px 6px;border-radius:8px;color:#9fb6b3;font-size:14px}.dk-home b{color:#fff;font-weight:600}.dk-home img{border-radius:6px;display:block}.dk-home:hover{background:#22302f}' +
    '.dk-tag{padding:4px 8px;border-radius:6px;background:#fafafa;color:#0f1a1a;font-weight:700;font-size:11px;letter-spacing:.06em;text-transform:uppercase}' +
    '.dk-themes{flex:1;min-width:0;display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;mask-image:linear-gradient(90deg,#000 92%,transparent)}.dk-themes::-webkit-scrollbar{display:none}' +
    '.dk-pill{flex:none;display:inline-flex;align-items:center;gap:6px;padding:7px 11px;border-radius:999px;border:1px solid #3a4b4a;color:#d4dedd;white-space:nowrap;transition:background .15s,border-color .15s}' +
    '.dk-pill:hover{border-color:#9fb6b3;color:#fff}.dk-pill[aria-current=page]{background:#fafafa;border-color:#fafafa;color:#0f1a1a}' +
    '.dk-pill small{font-size:11px;opacity:.7;font-weight:400}' +
    '.dk-admin{flex:none;display:inline-flex;align-items:center;gap:6px;white-space:nowrap;padding:7px 11px;border-radius:999px;background:#0E7C72;color:#fff!important;font-weight:600;font-size:12px}.dk-admin:hover{filter:brightness(1.12)}' +
    '.dk-turnkey{flex:none;white-space:nowrap;padding:7px 4px;color:#9fb6b3!important;font-size:12px}.dk-turnkey:hover{color:#fff!important}@media (max-width:1180px){.dk-turnkey{display:none}}' +
    '.dk-buy{flex:none;display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:8px;background:#fafafa;color:#0f1a1a!important;font-weight:600;white-space:nowrap}.dk-buy:hover{background:#e4e4e7}' +
    '.dk-short{display:none}@media (max-width:760px){.dk-admin span{display:none}}@media (max-width:640px){.dk-home span,.dk-tag,.dk-pill small,.dk-long{display:none}.dk-short{display:inline}}' +
    '.dk-wm{position:fixed;inset:0;z-index:2147482999;pointer-events:none;background-image:url("data:image/svg+xml,' +
    encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="440" height="260"><text x="30" y="150" transform="rotate(-24 220 130)" font-family="system-ui,sans-serif" font-size="15" font-weight="600" letter-spacing="2" fill="rgb(128,128,128)" fill-opacity="0.08">DEMO · stomatologie.devhub.md</text></svg>') +
    '")}@media print{.dk-bar,.dk-wm{display:none}}';

  function el(tag, attrs, html) {
    var e = document.createElement(tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (html != null) e.innerHTML = html;
    return e;
  }
  function mount() {
    if (document.querySelector('.dk-bar')) return;
    document.head.appendChild(el('style', { id: 'dk-style' }, css));
    var bar = el('nav', { 'class': 'dk-bar', 'aria-label': t.nav });
    bar.appendChild(el('a', { 'class': 'dk-home', href: home, title: t.all, 'aria-label': t.all },
      '<img src="/favicon.svg" width="22" height="22" alt=""><span><b>stomatologie</b>.devhub.md</span>'));
    bar.appendChild(el('span', { 'class': 'dk-tag' }, t.demo));
    var list = el('div', { 'class': 'dk-themes' });
    THEMES.forEach(function (x) {
      var a = el('a', { 'class': 'dk-pill', href: '/' + x.id + '/' + sub }, x.name + ' <small>' + (x.tag[lang] || x.tag.ro) + '</small>');
      if (x.id === theme.id) a.setAttribute('aria-current', 'page');
      list.appendChild(a);
    });
    bar.appendChild(list);
    bar.appendChild(el('a', { 'class': 'dk-admin', href: '/' + theme.id + '/admin/', title: t.admin },
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="7" height="9" rx="1"/><rect x="14" y="3" width="7" height="5" rx="1"/><rect x="14" y="12" width="7" height="9" rx="1"/><rect x="3" y="16" width="7" height="5" rx="1"/></svg><span>' + t.admin + '</span>'));
    bar.appendChild(el('a', { 'class': 'dk-turnkey', href: home + '#pricing' }, t.turnkey));
    bar.appendChild(el('a', { 'class': 'dk-buy', href: theme.buy, target: '_blank', rel: 'noopener' },
      '<span class="dk-long">' + t.buy + '</span><span class="dk-short">' + t.buyShort + '</span> →'));
    document.body.insertBefore(bar, document.body.firstChild);
    document.body.appendChild(el('div', { 'class': 'dk-wm', 'aria-hidden': 'true' }));
  }
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
})();
