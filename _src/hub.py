# Generates the stomatologie.devhub.md hub in 5 languages: / (ro), /en/, /ru/, /it/, /uk/
import json, os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://stomatologie.devhub.md/'
LANGS = ['ro', 'en', 'ru', 'it', 'uk']
LOCALE = {'ro': 'ro_RO', 'en': 'en_US', 'ru': 'ru_RU', 'it': 'it_IT', 'uk': 'uk_UA'}
NAMES = {'ro': 'Română', 'en': 'English', 'ru': 'Русский', 'it': 'Italiano', 'uk': 'Українська'}
STAN = 'https://stan.store/devhubmd'
BUY = STAN          # replace with the Stan product link once it exists
TURNKEY = STAN      # replace with the Stan "turnkey" product link
PRICE, TURNKEY_FROM = 99, 300
COUNTRIES = ['MD', 'RO', 'IT', 'UA', 'DE', 'GB', 'US']

T = {
 'ro': dict(
  title='Site pentru clinică stomatologică cu panou de administrare — 99 €',
  desc='Site gata pentru stomatologie în 5 limbi, cu panou de administrare, programări online și SEO. Găzduire gratuită pe GitHub Pages. 99 € sau la cheie de la 300 €.',
  eyebrow='Site-uri pentru stomatologii', h1='Site pentru clinica ta stomatologică, cu panou de administrare',
  lead='Landing rapid în 5 limbi, programări online și un panou în care schimbi singur prețuri, medici și texte. Fără server și fără abonament: rulează gratuit pe GitHub Pages.',
  demo='Vezi demo', admin='Încearcă panoul', buy=f'Cumpără · {PRICE} €', turnkey=f'La cheie de la {TURNKEY_FROM} €',
  incl_h='Ce primești', incl=[
   ('Landing complet', 'Servicii cu prețuri „de la”, medici, listă de prețuri, recenzii, întrebări, programare, contacte și program.'),
   ('Panou de administrare', 'Clinica schimbă singură textele, prețurile, pozele și medicii. Butonul „Publică” actualizează site-ul în un minut.'),
   ('5 limbi', 'Română, engleză, rusă, italiană și ucraineană, fiecare cu adresa ei. Le pornești sau oprești din panou.'),
   ('Programări', 'Formular pe email sau Telegram, plus WhatsApp, Viber, telefon, Rezervaora.md sau orice link extern.'),
   ('SEO de la început', 'Pagini statice pentru fiecare limbă, schema.org pentru stomatologie, hreflang, sitemap și întrebări frecvente.'),
   ('Cod curat', 'Vue 3 și Vite, panou pe shadcn-vue. Tot conținutul stă într-un singur fișier JSON.'),
  ],
  price_h='Prețuri', p1_name='Site + panou', p1_note='plată unică', p1=['Codul sursă complet', 'Panoul de administrare', '5 limbi și SEO', 'Găzduire gratuită pe GitHub Pages', 'Ghid de instalare pas cu pas'],
  p2_name='La cheie', p2_from='de la', p2_note='pentru clinica ta', p2=['Instalăm pe domeniul tău', 'Completăm textele, prețurile și medicii', 'Traducerile în limbile alese', 'Programările pe email sau Telegram', 'Google Search Console și Google Business', '30 de zile de suport'],
  steps_h='Cum funcționează', steps=[('Alegi varianta', 'Cumperi codul sau varianta la cheie.'), ('Publici pe GitHub', 'Încarci fișierele, pornești GitHub Pages; ghidul arată fiecare pas.'), ('Editezi din panou', 'Deschizi /admin/, schimbi ce vrei și apeși „Salvează și publică”.')],
  admin_h='Panoul de administrare', admin_p='Construit pe shadcn-vue. Merge pe telefon și pe calculator, în 5 limbi. Previzualizezi modificările înainte să le publici.',
  faq_h='Întrebări frecvente', faq=[
   ('Am nevoie de server sau hosting plătit?', 'Nu. Site-ul și panoul rulează gratuit pe GitHub Pages. Plătești doar domeniul, dacă vrei unul propriu.'),
   ('Cum ajung programările la noi?', 'Pe email prin Web3Forms (gratuit) sau în Telegram printr-un webhook. Pacienții pot scrie și pe WhatsApp, Viber sau suna direct.'),
   ('Pot pune domeniul meu?', 'Da. Adaugi fișierul CNAME și o înregistrare DNS; ghidul explică exact cum.'),
   ('Cine poate edita site-ul?', 'Oricine are tokenul GitHub al clinicii. Tokenul stă doar în browserul celui care editează.'),
   ('Vor fi și alte design-uri?', 'Da. Motorul e comun, iar design-urile noi se adaugă ca teme. Primul design este Lumen.'),
  ],
  footer='Site-uri pentru saloane de frumusețe', demo_label='Design Lumen · demo', langs='Limbi'),
 'en': dict(
  title='Dental clinic website with admin panel — €99',
  desc='A ready dental clinic website in 5 languages with an admin panel, online booking and SEO. Free hosting on GitHub Pages. €99, or done for you from €300.',
  eyebrow='Websites for dental clinics', h1='A website for your dental clinic, with its own admin panel',
  lead='A fast landing page in 5 languages, online booking and a panel where you change prices, doctors and texts yourself. No server and no subscription: it runs free on GitHub Pages.',
  demo='View demo', admin='Try the admin', buy=f'Buy · €{PRICE}', turnkey=f'Done for you from €{TURNKEY_FROM}',
  incl_h='What you get', incl=[
   ('Complete landing page', 'Services with "from" prices, doctors, price list, reviews, FAQ, booking, contacts and opening hours.'),
   ('Admin panel', 'The clinic updates texts, prices, photos and doctors. "Publish" updates the site in about a minute.'),
   ('5 languages', 'Romanian, English, Russian, Italian and Ukrainian, each at its own address. Turn them on or off in the panel.'),
   ('Booking', 'A form to email or Telegram, plus WhatsApp, Viber, phone, Rezervaora.md or any external link.'),
   ('SEO from day one', 'Static pages per language, schema.org for dentists, hreflang, sitemap and FAQ markup.'),
   ('Clean code', 'Vue 3 and Vite, admin built on shadcn-vue. All content lives in one JSON file.'),
  ],
  price_h='Pricing', p1_name='Website + admin', p1_note='one-time payment', p1=['Full source code', 'Admin panel', '5 languages and SEO', 'Free hosting on GitHub Pages', 'Step-by-step install guide'],
  p2_name='Done for you', p2_from='from', p2_note='for your clinic', p2=['Installed on your domain', 'Your texts, prices and doctors filled in', 'Translations into your languages', 'Booking to email or Telegram', 'Google Search Console and Google Business', '30 days of support'],
  steps_h='How it works', steps=[('Choose', 'Buy the code or the done-for-you option.'), ('Publish on GitHub', 'Upload the files and turn on GitHub Pages; the guide shows every step.'), ('Edit in the panel', 'Open /admin/, change what you need and press "Save and publish".')],
  admin_h='The admin panel', admin_p='Built on shadcn-vue. Works on phone and desktop, in 5 languages. Preview changes before you publish them.',
  faq_h='Frequently asked questions', faq=[
   ('Do I need a server or paid hosting?', 'No. The site and the admin run free on GitHub Pages. You only pay for a domain if you want your own.'),
   ('How do booking requests reach us?', 'By email through Web3Forms (free) or in Telegram through a webhook. Patients can also message on WhatsApp, Viber or call.'),
   ('Can I use my own domain?', 'Yes. Add a CNAME file and one DNS record; the guide explains how.'),
   ('Who can edit the site?', 'Anyone with the clinic\'s GitHub token. The token is stored only in the editor\'s browser.'),
   ('Will there be other designs?', 'Yes. The engine is shared and new designs are added as themes. The first design is Lumen.'),
  ],
  footer='Websites for beauty salons', demo_label='Lumen design · demo', langs='Languages'),
 'ru': dict(
  title='Сайт для стоматологии с панелью управления — 99 €',
  desc='Готовый сайт для стоматологии на 5 языках с панелью управления, онлайн-записью и SEO. Бесплатный хостинг на GitHub Pages. 99 € или под ключ от 300 €.',
  eyebrow='Сайты для стоматологий', h1='Сайт для вашей стоматологии с собственной панелью управления',
  lead='Быстрый лендинг на 5 языках, онлайн-запись и панель, где вы сами меняете цены, врачей и тексты. Без сервера и подписки: работает бесплатно на GitHub Pages.',
  demo='Смотреть демо', admin='Попробовать панель', buy=f'Купить · {PRICE} €', turnkey=f'Под ключ от {TURNKEY_FROM} €',
  incl_h='Что входит', incl=[
   ('Готовый лендинг', 'Услуги с ценами «от», врачи, прайс, отзывы, вопросы, запись, контакты и часы работы.'),
   ('Панель управления', 'Клиника сама меняет тексты, цены, фото и врачей. Кнопка «Опубликовать» обновляет сайт за минуту.'),
   ('5 языков', 'Румынский, английский, русский, итальянский и украинский, у каждого свой адрес. Включаются в панели.'),
   ('Запись', 'Форма на почту или в Telegram, плюс WhatsApp, Viber, телефон, Rezervaora.md или любая внешняя ссылка.'),
   ('SEO с первого дня', 'Статичные страницы на каждом языке, schema.org для стоматологии, hreflang, sitemap и разметка FAQ.'),
   ('Чистый код', 'Vue 3 и Vite, панель на shadcn-vue. Весь контент в одном JSON-файле.'),
  ],
  price_h='Цены', p1_name='Сайт + панель', p1_note='разовая оплата', p1=['Полный исходный код', 'Панель управления', '5 языков и SEO', 'Бесплатный хостинг на GitHub Pages', 'Пошаговая инструкция'],
  p2_name='Под ключ', p2_from='от', p2_note='для вашей клиники', p2=['Установка на ваш домен', 'Заполним тексты, цены и врачей', 'Переводы на нужные языки', 'Заявки на почту или в Telegram', 'Google Search Console и Google Business', '30 дней поддержки'],
  steps_h='Как это работает', steps=[('Выбираете', 'Покупаете код или вариант под ключ.'), ('Публикуете на GitHub', 'Загружаете файлы и включаете GitHub Pages; инструкция показывает каждый шаг.'), ('Редактируете в панели', 'Открываете /admin/, меняете что нужно и нажимаете «Сохранить и опубликовать».')],
  admin_h='Панель управления', admin_p='Сделана на shadcn-vue. Работает на телефоне и компьютере, на 5 языках. Предпросмотр изменений до публикации.',
  faq_h='Частые вопросы', faq=[
   ('Нужен ли сервер или платный хостинг?', 'Нет. Сайт и панель работают бесплатно на GitHub Pages. Платите только за домен, если нужен свой.'),
   ('Как к нам приходят заявки?', 'На почту через Web3Forms (бесплатно) или в Telegram через webhook. Пациенты также могут написать в WhatsApp, Viber или позвонить.'),
   ('Можно подключить свой домен?', 'Да. Добавляете файл CNAME и одну DNS-запись; инструкция объясняет как.'),
   ('Кто может редактировать сайт?', 'Тот, у кого есть токен GitHub клиники. Токен хранится только в браузере редактора.'),
   ('Будут другие дизайны?', 'Да. Движок общий, новые дизайны добавляются как темы. Первый дизайн — Lumen.'),
  ],
  footer='Сайты для салонов красоты', demo_label='Дизайн Lumen · демо', langs='Языки'),
 'it': dict(
  title='Sito per studio dentistico con pannello di gestione — 99 €',
  desc='Sito pronto per studi dentistici in 5 lingue, con pannello di gestione, prenotazioni online e SEO. Hosting gratuito su GitHub Pages. 99 € o chiavi in mano da 300 €.',
  eyebrow='Siti per studi dentistici', h1='Un sito per il tuo studio dentistico, con il suo pannello di gestione',
  lead='Una landing veloce in 5 lingue, prenotazioni online e un pannello dove cambi da solo prezzi, medici e testi. Niente server né abbonamento: gira gratis su GitHub Pages.',
  demo='Guarda la demo', admin='Prova il pannello', buy=f'Acquista · {PRICE} €', turnkey=f'Chiavi in mano da {TURNKEY_FROM} €',
  incl_h='Cosa ottieni', incl=[
   ('Landing completa', 'Servizi con prezzi "da", medici, listino, recensioni, domande, prenotazione, contatti e orari.'),
   ('Pannello di gestione', 'Lo studio aggiorna testi, prezzi, foto e medici. "Pubblica" aggiorna il sito in circa un minuto.'),
   ('5 lingue', 'Rumeno, inglese, russo, italiano e ucraino, ognuna al suo indirizzo. Si attivano dal pannello.'),
   ('Prenotazioni', 'Modulo via email o Telegram, più WhatsApp, Viber, telefono, Rezervaora.md o qualsiasi link esterno.'),
   ('SEO dal primo giorno', 'Pagine statiche per lingua, schema.org per dentisti, hreflang, sitemap e markup FAQ.'),
   ('Codice pulito', 'Vue 3 e Vite, pannello su shadcn-vue. Tutti i contenuti in un solo file JSON.'),
  ],
  price_h='Prezzi', p1_name='Sito + pannello', p1_note='pagamento unico', p1=['Codice sorgente completo', 'Pannello di gestione', '5 lingue e SEO', 'Hosting gratuito su GitHub Pages', 'Guida di installazione passo per passo'],
  p2_name='Chiavi in mano', p2_from='da', p2_note='per il tuo studio', p2=['Installazione sul tuo dominio', 'Testi, prezzi e medici inseriti da noi', 'Traduzioni nelle lingue scelte', 'Prenotazioni via email o Telegram', 'Google Search Console e Google Business', '30 giorni di assistenza'],
  steps_h='Come funziona', steps=[('Scegli', 'Acquisti il codice o la versione chiavi in mano.'), ('Pubblichi su GitHub', 'Carichi i file e attivi GitHub Pages; la guida mostra ogni passo.'), ('Modifichi dal pannello', 'Apri /admin/, cambi ciò che serve e premi "Salva e pubblica".')],
  admin_h='Il pannello di gestione', admin_p='Costruito su shadcn-vue. Funziona su telefono e computer, in 5 lingue. Anteprima delle modifiche prima di pubblicarle.',
  faq_h='Domande frequenti', faq=[
   ('Serve un server o un hosting a pagamento?', 'No. Sito e pannello girano gratis su GitHub Pages. Paghi solo il dominio, se ne vuoi uno tuo.'),
   ('Come arrivano le prenotazioni?', 'Via email con Web3Forms (gratis) o su Telegram con un webhook. I pazienti possono anche scrivere su WhatsApp, Viber o chiamare.'),
   ('Posso usare il mio dominio?', 'Sì. Aggiungi un file CNAME e un record DNS; la guida spiega come.'),
   ('Chi può modificare il sito?', 'Chi ha il token GitHub dello studio. Il token resta solo nel browser di chi modifica.'),
   ('Ci saranno altri design?', 'Sì. Il motore è comune e i nuovi design si aggiungono come temi. Il primo design è Lumen.'),
  ],
  footer='Siti per saloni di bellezza', demo_label='Design Lumen · demo', langs='Lingue'),
 'uk': dict(
  title='Сайт для стоматології з панеллю керування — 99 €',
  desc='Готовий сайт для стоматології 5 мовами з панеллю керування, онлайн-записом і SEO. Безкоштовний хостинг на GitHub Pages. 99 € або під ключ від 300 €.',
  eyebrow='Сайти для стоматологій', h1='Сайт для вашої стоматології з власною панеллю керування',
  lead='Швидкий лендинг 5 мовами, онлайн-запис і панель, де ви самі змінюєте ціни, лікарів і тексти. Без сервера й підписки: працює безкоштовно на GitHub Pages.',
  demo='Дивитися демо', admin='Спробувати панель', buy=f'Купити · {PRICE} €', turnkey=f'Під ключ від {TURNKEY_FROM} €',
  incl_h='Що входить', incl=[
   ('Готовий лендинг', 'Послуги з цінами «від», лікарі, прайс, відгуки, питання, запис, контакти та графік роботи.'),
   ('Панель керування', 'Клініка сама змінює тексти, ціни, фото й лікарів. Кнопка «Опублікувати» оновлює сайт за хвилину.'),
   ('5 мов', 'Румунська, англійська, російська, італійська та українська, кожна за своєю адресою. Вмикаються в панелі.'),
   ('Запис', 'Форма на пошту або в Telegram, а також WhatsApp, Viber, телефон, Rezervaora.md чи будь-яке зовнішнє посилання.'),
   ('SEO з першого дня', 'Статичні сторінки кожною мовою, schema.org для стоматології, hreflang, sitemap і розмітка FAQ.'),
   ('Чистий код', 'Vue 3 і Vite, панель на shadcn-vue. Увесь контент в одному JSON-файлі.'),
  ],
  price_h='Ціни', p1_name='Сайт + панель', p1_note='разова оплата', p1=['Повний вихідний код', 'Панель керування', '5 мов і SEO', 'Безкоштовний хостинг на GitHub Pages', 'Покрокова інструкція'],
  p2_name='Під ключ', p2_from='від', p2_note='для вашої клініки', p2=['Встановлення на ваш домен', 'Заповнимо тексти, ціни й лікарів', 'Переклади потрібними мовами', 'Заявки на пошту або в Telegram', 'Google Search Console і Google Business', '30 днів підтримки'],
  steps_h='Як це працює', steps=[('Обираєте', 'Купуєте код або варіант під ключ.'), ('Публікуєте на GitHub', 'Завантажуєте файли й вмикаєте GitHub Pages; інструкція показує кожен крок.'), ('Редагуєте в панелі', 'Відкриваєте /admin/, змінюєте потрібне й натискаєте «Зберегти й опублікувати».')],
  admin_h='Панель керування', admin_p='Зроблена на shadcn-vue. Працює на телефоні й комп’ютері, 5 мовами. Попередній перегляд змін до публікації.',
  faq_h='Часті питання', faq=[
   ('Чи потрібен сервер або платний хостинг?', 'Ні. Сайт і панель працюють безкоштовно на GitHub Pages. Платите лише за домен, якщо потрібен власний.'),
   ('Як до нас надходять заявки?', 'На пошту через Web3Forms (безкоштовно) або в Telegram через webhook. Пацієнти також можуть написати у WhatsApp, Viber або зателефонувати.'),
   ('Чи можна підключити свій домен?', 'Так. Додаєте файл CNAME та один DNS-запис; інструкція пояснює як.'),
   ('Хто може редагувати сайт?', 'Той, хто має токен GitHub клініки. Токен зберігається лише в браузері редактора.'),
   ('Чи будуть інші дизайни?', 'Так. Рушій спільний, нові дизайни додаються як теми. Перший дизайн — Lumen.'),
  ],
  footer='Сайти для салонів краси', demo_label='Дизайн Lumen · демо', langs='Мови'),
}

def path(l): return '' if l == 'ro' else l + '/'
def demo(l): return f'/lumen/{path(l)}'
e = html.escape

def ld(l, t):
    url = SITE + path(l)
    policy = {'@type': 'MerchantReturnPolicy', 'applicableCountry': COUNTRIES, 'returnPolicyCategory': 'https://schema.org/MerchantReturnNotPermitted'}
    ship = {'@type': 'OfferShippingDetails', 'shippingRate': {'@type': 'MonetaryAmount', 'value': '0', 'currency': 'EUR'},
            'shippingDestination': [{'@type': 'DefinedRegion', 'addressCountry': c} for c in COUNTRIES],
            'deliveryTime': {'@type': 'ShippingDeliveryTime', 'handlingTime': {'@type': 'QuantitativeValue', 'minValue': 0, 'maxValue': 0, 'unitCode': 'DAY'},
                             'transitTime': {'@type': 'QuantitativeValue', 'minValue': 0, 'maxValue': 0, 'unitCode': 'DAY'}}}
    g = [
        {'@type': 'WebSite', '@id': SITE + '#website', 'url': SITE, 'name': 'stomatologie.devhub.md', 'inLanguage': LANGS,
         'publisher': {'@type': 'Organization', 'name': 'devhub.md', 'url': 'https://devhub.md/'}},
        {'@type': 'WebPage', '@id': url + '#webpage', 'url': url, 'name': t['title'], 'description': t['desc'], 'inLanguage': l, 'isPartOf': {'@id': SITE + '#website'},
         'primaryImageOfPage': SITE + 'img/og.jpg'},
        {'@type': 'Product', 'name': t['p1_name'] + ' — Lumen', 'description': t['desc'], 'image': SITE + 'img/lumen-desktop.webp', 'brand': {'@type': 'Brand', 'name': 'devhub.md'},
         'offers': {'@type': 'Offer', 'price': str(PRICE), 'priceCurrency': 'EUR', 'availability': 'https://schema.org/InStock', 'url': BUY,
                    'hasMerchantReturnPolicy': policy, 'shippingDetails': ship}},
        {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in t['faq']]},
    ]
    return json.dumps({'@context': 'https://schema.org', '@graph': g}, ensure_ascii=False).replace('<', '\\u003c')

CSS = open(os.path.join(ROOT, '_src', 'hub.css')).read()

def page(l):
    t = T[l]
    alt = '\n'.join(f'<link rel="alternate" hreflang="{x}" href="{SITE + path(x)}">' for x in LANGS)
    langs = ''.join(f'<a href="/{path(x)}" hreflang="{x}"{" aria-current=page" if x == l else ""}>{x.upper()}</a>' for x in LANGS)
    incl = ''.join(f'<li><h3>{e(a)}</h3><p>{e(b)}</p></li>' for a, b in t['incl'])
    p1 = ''.join(f'<li>{e(x)}</li>' for x in t['p1'])
    p2 = ''.join(f'<li>{e(x)}</li>' for x in t['p2'])
    steps = ''.join(f'<li><span>{i + 1}</span><h3>{e(a)}</h3><p>{e(b)}</p></li>' for i, (a, b) in enumerate(t['steps']))
    faq = ''.join(f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><p>{e(a)}</p></details>' for i, (q, a) in enumerate(t['faq']))
    salon = 'https://salon.devhub.md/' + ('' if l in ('ro', 'en', 'uk') else l + '/')
    return f'''<!doctype html>
<html lang="{l}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(t['title'])}</title>
<meta name="description" content="{e(t['desc'])}">
<link rel="canonical" href="{SITE + path(l)}">
{alt}
<link rel="alternate" hreflang="x-default" href="{SITE}">
<meta property="og:type" content="website"><meta property="og:title" content="{e(t['title'])}"><meta property="og:description" content="{e(t['desc'])}">
<meta property="og:url" content="{SITE + path(l)}"><meta property="og:image" content="{SITE}img/og.jpg"><meta property="og:locale" content="{LOCALE[l]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preload" href="/fonts/onest-latin.woff2" as="font" type="font/woff2" crossorigin>
<style>{CSS}</style>
<script type="application/ld+json">{ld(l, t)}</script>
</head>
<body>
<header class="hd"><div class="w hd__row">
  <a class="logo" href="/{path(l)}"><span class="logo__m"></span>stomatologie<span class="logo__d">.devhub.md</span></a>
  <nav class="langs" aria-label="{e(t['langs'])}">{langs}</nav>
</div></header>
<main>
<section class="hero"><div class="w hero__g">
  <div class="hero__t">
    <p class="eb">{e(t['eyebrow'])}</p>
    <h1>{e(t['h1'])}</h1>
    <p class="lead">{e(t['lead'])}</p>
    <div class="ctas"><a class="btn btn--p" href="{BUY}">{e(t['buy'])}</a><a class="btn btn--g" href="{demo(l)}">{e(t['demo'])} →</a></div>
    <p class="sub"><a href="{TURNKEY}">{e(t['turnkey'])}</a> · <a href="/lumen/admin/">{e(t['admin'])}</a></p>
  </div>
  <a class="shots" href="{demo(l)}" aria-label="{e(t['demo'])}">
    <img class="shots__d" src="/img/lumen-desktop.webp" width="1200" height="750" alt="{e(t['demo_label'])}" fetchpriority="high">
    <img class="shots__m" src="/img/lumen-mobile.webp" width="390" height="780" alt="" loading="lazy">
    <span class="shots__l">{e(t['demo_label'])}</span>
  </a>
</div></section>
<section class="sec"><div class="w"><h2>{e(t['incl_h'])}</h2><ul class="incl">{incl}</ul></div></section>
<section class="sec sec--admin"><div class="w adm">
  <div><h2>{e(t['admin_h'])}</h2><p class="lead">{e(t['admin_p'])}</p><a class="btn btn--g" href="/lumen/admin/">{e(t['admin'])} →</a></div>
  <img src="/img/admin.webp" width="1200" height="750" alt="{e(t['admin_h'])}" loading="lazy">
</div></section>
<section class="sec" id="pricing"><div class="w"><h2>{e(t['price_h'])}</h2>
  <div class="plans">
    <div class="plan"><h3>{e(t['p1_name'])}</h3><p class="pr">{PRICE} €<small>{e(t['p1_note'])}</small></p><ul>{p1}</ul><a class="btn btn--p" href="{BUY}">{e(t['buy'])}</a></div>
    <div class="plan plan--dark"><h3>{e(t['p2_name'])}</h3><p class="pr"><small>{e(t['p2_from'])}</small> {TURNKEY_FROM} €<small>{e(t['p2_note'])}</small></p><ul>{p2}</ul><a class="btn btn--w" href="{TURNKEY}">{e(t['turnkey'])}</a></div>
  </div>
</div></section>
<section class="sec"><div class="w"><h2>{e(t['steps_h'])}</h2><ol class="steps">{steps}</ol></div></section>
<section class="sec"><div class="w faq"><h2>{e(t['faq_h'])}</h2><div>{faq}</div></div></section>
</main>
<footer class="ft"><div class="w ft__row">
  <span>© 2026 <a href="https://devhub.md/">devhub.md</a></span>
  <a href="{salon}">{e(t['footer'])} → salon.devhub.md</a>
</div></footer>
</body>
</html>
'''

for l in LANGS:
    d = os.path.join(ROOT, path(l))
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w').write(page(l))
open(os.path.join(ROOT, '404.html'), 'w').write(page('ro'))

urls = [SITE + path(l) for l in LANGS] + [SITE + 'lumen/' + path(l) for l in LANGS]
def alts(prefix): return ''.join(f'<xhtml:link rel="alternate" hreflang="{x}" href="{SITE}{prefix}{path(x)}"/>' for x in LANGS)
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for prefix in ['', 'lumen/']:
    for l in LANGS:
        sm.append(f'<url><loc>{SITE}{prefix}{path(l)}</loc>{alts(prefix)}</url>')
sm.append('</urlset>')
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('\n'.join(sm) + '\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /lumen/admin/\nSitemap: {SITE}sitemap.xml\n')
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')
print('hub ok')
