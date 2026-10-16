import json,re
m=json.load(open('meta.json'))
for f in ('gh2.json','gh.json'):
    for k,v in json.load(open(f)).items(): m.setdefault(k.lower(),v)
from new_entries import N
OFF={'ClickHouse/mcp-clickhouse','cloud-ru/mcp-servers','timeweb-cloud/mcp-server','sendpulse/mcp-server','vkustech/vkusvill-mcp-server-manifest','ai-forever/mcp_kandinsky','salute-developers/plasma-mcp-server'}
C=dict(mp="Маркетплейсы",ads="Реклама и аналитика",ai="ИИ и LLM",bank="Банки и платежи",acc="1С и учёт",crm="CRM и продажи",msg="Мессенджеры и соцсети",hr="HR и рекрутинг",log="Логистика и доставка",biz="Данные о компаниях и право",cloud="Облака и DevOps",dev="Разработка",web="Поиск и веб",db="Базы данных",prod="Продуктивность и документы",tel="Связь и рассылки",ya="Сервисы Яндекса")
# repo, slug, name, cat, service, desc, official, install(kind,value)
R=[
# general
("modelcontextprotocol/servers","filesystem","Filesystem (официальный)","dev","Файловая система","Эталонный сервер MCP: безопасное чтение и запись файлов в разрешённых каталогах.",True,("npx","@modelcontextprotocol/server-filesystem /path/to/dir"),"modelcontextprotocol/servers/tree/main/src/filesystem"),
("modelcontextprotocol/servers","memory","Memory (официальный)","ai","Память агента","Долговременная память агента на основе графа знаний.",True,("npx","@modelcontextprotocol/server-memory"),"modelcontextprotocol/servers/tree/main/src/memory"),
("modelcontextprotocol/servers","sequential-thinking","Sequential Thinking","ai","Рассуждения","Инструмент пошагового рассуждения и пересмотра гипотез для сложных задач.",True,("npx","@modelcontextprotocol/server-sequential-thinking"),"modelcontextprotocol/servers/tree/main/src/sequentialthinking"),
("modelcontextprotocol/servers","fetch","Fetch","web","Загрузка веб-страниц","Загружает веб-страницы и конвертирует их в Markdown для модели.",True,("uvx","mcp-server-fetch"),"modelcontextprotocol/servers/tree/main/src/fetch"),
("modelcontextprotocol/servers","git","Git","dev","Git","Чтение, поиск и операции с локальными Git-репозиториями.",True,("uvx","mcp-server-git"),"modelcontextprotocol/servers/tree/main/src/git"),
("modelcontextprotocol/servers","time","Time","prod","Время и часовые пояса","Текущее время и конвертация между часовыми поясами.",True,("uvx","mcp-server-time"),"modelcontextprotocol/servers/tree/main/src/time"),
("modelcontextprotocol/servers","everything","Everything (тестовый)","dev","Тестирование MCP","Тестовый сервер со всеми возможностями протокола — для разработчиков клиентов.",True,("npx","@modelcontextprotocol/server-everything"),"modelcontextprotocol/servers/tree/main/src/everything"),
("github/github-mcp-server","github","GitHub","dev","GitHub","Официальный сервер GitHub: репозитории, issues, PR, Actions и поиск кода.",True,("http","https://api.githubcopilot.com/mcp/"),None),
("microsoft/playwright-mcp","playwright","Playwright","web","Браузер","Управление браузером через Playwright: навигация, клики, формы, снимки доступности.",True,("npx","@playwright/mcp@latest"),None),
("upstash/context7","context7","Context7","dev","Документация библиотек","Актуальная документация и примеры кода библиотек прямо в контексте модели.",True,("http","https://mcp.context7.com/mcp"),None),
("supabase/mcp","supabase","Supabase","db","Supabase","Управление проектами Supabase: таблицы, SQL, миграции, edge-функции.",True,("http","https://mcp.supabase.com/mcp"),None),
("stripe/ai","stripe","Stripe","bank","Stripe","Официальный сервер Stripe: платежи, клиенты, подписки и документация.",True,("http","https://mcp.stripe.com"),None),
("getsentry/toolkit","sentry","Sentry","dev","Sentry","Ошибки и инциденты из Sentry, анализ стектрейсов.",True,("http","https://mcp.sentry.dev/mcp"),None),
("cloudflare/mcp-server-cloudflare","cloudflare","Cloudflare","cloud","Cloudflare","Набор серверов Cloudflare: Workers, документация, логи, DNS и др.",True,("http","https://docs.mcp.cloudflare.com/mcp"),None),
("makenotion/notion-mcp-server","notion","Notion","prod","Notion","Официальный сервер Notion: поиск, чтение и редактирование страниц и баз.",True,("http","https://mcp.notion.com/mcp"),None),
("sooperset/mcp-atlassian","atlassian","Atlassian (Jira, Confluence)","prod","Jira / Confluence","Работа с задачами Jira и страницами Confluence (Cloud и Server/DC).",False,("uvx","mcp-atlassian"),None),
("firecrawl/firecrawl-mcp-server","firecrawl","Firecrawl","web","Firecrawl","Скрапинг и краулинг сайтов, извлечение структурированных данных.",True,("npx","firecrawl-mcp"),None),
("exa-labs/exa-mcp-server","exa","Exa Search","web","Exa","Нейропоиск по вебу и коду через Exa API.",True,("http","https://mcp.exa.ai/mcp"),None),
("brave/brave-search-mcp-server","brave-search","Brave Search","web","Brave Search","Веб-, новостной и локальный поиск через Brave Search API.",True,("npx","@brave/brave-search-mcp-server"),None),
("ChromeDevTools/chrome-devtools-mcp","chrome-devtools","Chrome DevTools","dev","Chrome","Отладка в Chrome: консоль, сеть, производительность, скриншоты.",True,("npx","chrome-devtools-mcp@latest"),None),
("microsoft/markitdown","markitdown","MarkItDown","prod","Конвертация документов","Конвертирует PDF, DOCX, XLSX, PPTX и другие файлы в Markdown.",True,("uvx","markitdown-mcp"),"microsoft/markitdown/tree/main/packages/markitdown-mcp"),
("mongodb-js/mongodb-mcp-server","mongodb","MongoDB","db","MongoDB","Запросы и администрирование MongoDB и Atlas.",True,("npx","mongodb-mcp-server"),None),
("redis/mcp-redis","redis","Redis","db","Redis","Работа с данными Redis на естественном языке.",True,("uvx","--from redis-mcp-server@latest redis-mcp-server --url redis://localhost:6379/0"),None),
("hashicorp/terraform-mcp-server","terraform","Terraform","cloud","Terraform","Поиск провайдеров и модулей Terraform Registry, работа с HCP Terraform.",True,("docker","hashicorp/terraform-mcp-server"),None),
("awslabs/mcp","aws","AWS MCP Servers","cloud","AWS","Набор официальных серверов AWS: документация, CDK, стоимость, сервисы.",True,("uvx","awslabs.aws-documentation-mcp-server@latest"),None),
("googleapis/mcp-toolbox","google-mcp-toolbox","MCP Toolbox for Databases","db","Google / БД","Сервер Google для подключения агентов к PostgreSQL, MySQL, BigQuery и др.",True,("manual",None),None),
("korotovsky/slack-mcp-server","slack","Slack","msg","Slack","Чтение каналов, тредов и поиск сообщений в Slack.",False,("npx","slack-mcp-server@latest --transport stdio"),None),
("grafana/mcp-grafana","grafana","Grafana","cloud","Grafana","Дашборды, источники данных, Prometheus/Loki-запросы и алерты Grafana.",True,("manual",None),None),
("GLips/Figma-Context-MCP","figma-context","Figma Context","dev","Figma","Передаёт макеты Figma агенту для генерации вёрстки.",False,("npx","figma-developer-mcp --figma-api-key=YOUR_KEY --stdio"),None),
("oraios/serena","serena","Serena","dev","Код (LSP)","Семантическая навигация и правка кода через языковые серверы.",False,("uvx","--from git+https://github.com/oraios/serena serena start-mcp-server"),None),
("containers/kubernetes-mcp-server","kubernetes","Kubernetes","cloud","Kubernetes","Управление кластерами Kubernetes и OpenShift.",False,("npx","kubernetes-mcp-server@latest"),None),
("tavily-ai/tavily-mcp","tavily","Tavily","web","Tavily","Поиск и извлечение веб-контента для агентов.",True,("npx","tavily-mcp@latest"),None),
("browserbase/mcp-server-browserbase","browserbase","Browserbase","web","Browserbase","Облачный браузер для агентов (Stagehand).",True,("npx","@browserbasehq/mcp-server-browserbase"),None),
("docker/mcp-gateway","docker-mcp-gateway","Docker MCP Gateway","cloud","Docker","Шлюз Docker для запуска MCP-серверов в контейнерах.",True,("manual",None),None),
("PostHog/mcp","posthog","PostHog","ads","PostHog","Продуктовая аналитика PostHog: инсайты, фича-флаги, ошибки.",True,("http","https://mcp.posthog.com/mcp"),None),
("neondatabase/mcp-server-neon","neon","Neon","db","Neon Postgres","Управление базами Neon Postgres: ветки, SQL, миграции.",True,("http","https://mcp.neon.tech/mcp"),None),
("microsoft/azure-devops-mcp","azure-devops","Azure DevOps","dev","Azure DevOps","Работа с задачами, репозиториями и пайплайнами Azure DevOps.",True,("npx","@azure-devops/mcp YOUR_ORG"),None),
("apify/apify-mcp-server","apify","Apify","web","Apify","Тысячи готовых скраперов Apify как инструменты агента.",True,("http","https://mcp.apify.com"),None),
("elastic/mcp-server-elasticsearch","elasticsearch","Elasticsearch","db","Elasticsearch","Поиск и запросы к индексам Elasticsearch.",True,("manual",None),None),
# RU
("yandex-cloud/mcp","yandex-cloud","Yandex Cloud MCP Servers","cloud","Yandex Cloud","Официальные MCP-серверы Yandex Cloud: документация, ресурсы облака и сервисы.",True,("manual",None),None),
("yandex/yandex-search-mcp-server","yandex-search","Yandex Search (официальный)","ya","Яндекс Поиск","Официальный сервер веб-поиска Яндекса через Yandex Search API.",True,("manual",None),None),
("2gis/2gis-mcp","2gis","2GIS (официальный)","log","2ГИС","Сервер 2ГИС: поиск мест и организаций, геоданные.",True,("manual",None),None),
("bitrix24/mcp-rest-doc","bitrix24-docs","Bitrix24 REST Docs (официальный)","crm","Битрикс24","Официальный сервер Битрикс24 с актуальной документацией REST API для ИИ-ассистентов.",True,("manual",None),None),
("ai-forever/mcp_giga_checker","giga-checker","GigaChat AI-text Checker","ai","GigaChat (Сбер)","Определение сгенерированного ИИ текста через GigaChat API (команда ai-forever, Сбер).",True,("manual",None),None),
("alexsvdk/gigaplexity-mcp","gigaplexity","Gigaplexity","ai","GigaChat (Сбер)","Превращает GigaChat в поискового ассистента с доступом к вебу.",False,("manual",None),None),
("chigwell/telegram-mcp","telegram-chigwell","Telegram (Telethon)","msg","Telegram","Чтение чатов, отправка сообщений и управление группами Telegram через Telethon.",False,("manual",None),None),
("chaindead/telegram-mcp","telegram-chaindead","Telegram MCP (Go)","msg","Telegram","Диалоги, сообщения, черновики и статусы прочтения в Telegram.",False,("manual",None),None),
("bulatko/vk-mcp-server","vk","VK (ВКонтакте)","msg","ВКонтакте","Доступ к API ВКонтакте: пользователи, стены, сообщества.",False,("manual",None),None),
("askads/mcp-vk-ads","vk-ads-askads","VK Ads","ads","VK Реклама","Управление кампаниями, группами объявлений и статистикой VK Рекламы.",False,("manual",None),None),
("woyaxnini/mcp-max-messenger","max-messenger","MAX Messenger","msg","MAX","Сервер для национального мессенджера MAX (VK).",False,("manual",None),None),
("renosaza/max-mcp","max-user","MAX (пользовательская сессия)","msg","MAX","Чтение чатов и выгрузка каналов MAX через пользовательскую сессию.",False,("manual",None),None),
("vladimir-kharin/1c_mcp","1c-mcp-kharin","1C MCP (расширение)","acc","1С:Предприятие","Создание MCP-серверов внутри 1С:Предприятие через расширение конфигурации.",False,("manual",None),None),
("ROCTUP/1c-mcp-toolkit","1c-mcp-toolkit","1C MCP Toolkit","acc","1С:Предприятие","MCP и REST-сервер для метаданных и данных из базы 1С.",False,("manual",None),None),
("DitriXNew/EDT-MCP","1c-edt","EDT-MCP","acc","1С:EDT","MCP для среды разработки 1С:EDT.",False,("manual",None),None),
("feenlace/mcp-1c","mcp-1c-go","mcp-1c","acc","1С:Предприятие","Ассистент видит конфигурацию 1С и генерирует точный код BSL.",False,("manual",None),None),
("fserg/mcp-1c-v1","mcp-1c-rag","MCP 1C RAG","acc","1С:Предприятие","RAG-описание структуры конфигурации 1С для ИИ.",False,("manual",None),None),
("vgtitov/bsl-ai-toolkit","bsl-ai-toolkit","BSL AI Toolkit","acc","1С:Предприятие","Правила, скиллы и MCP-серверы для разработки на 1С (BSL).",False,("manual",None),None),
("Untru/1c-mcp","1c-mcp-list","1C MCP Awesome List","acc","1С:Предприятие","Каталог MCP-серверов экосистемы 1С (подборка).",False,("manual",None),None),
("kartochka/bitrix24-mcp","bitrix24-kartochka","Bitrix24 MCP","crm","Битрикс24","Работа с Битрикс24 на естественном языке: сделки, контакты, задачи.",False,("manual",None),None),
("gunnit/bitrix24-mcp-server","bitrix24-gunnit","Bitrix24 MCP Server","crm","Битрикс24","Полноценная интеграция с CRM Битрикс24.",False,("manual",None),None),
("bit2beat/bitrix24-mcp","bitrix24-bit2beat","Bitrix24 for Claude","crm","Битрикс24","CRM, задачи, диск, календарь и автоматизации Битрикс24.",False,("manual",None),None),
("grabarnick/amocrm-mcp-server","amocrm-grabarnick","amoCRM MCP Server","crm","amoCRM","Сделки, контакты и воронки amoCRM.",False,("manual",None),None),
("DocAtWork2026/amocrm-mcp","amocrm-docatwork","amoCRM MCP","crm","amoCRM","Интеграция amoCRM с Claude Desktop и другими клиентами.",False,("manual",None),None),
("gmen1057/headhunter-mcp-server","headhunter","HeadHunter MCP","hr","HeadHunter","Поиск вакансий, управление резюме и откликами через API hh.ru.",False,("manual",None),None),
("antalez/hh-cv-mcp","hh-cv","hh.ru CV MCP","hr","HeadHunter","Поиск, резюме, отклики и переписка с работодателями на hh.ru.",False,("manual",None),None),
("Vladimir-Human/ru-marketplace-mcp","ru-marketplace","RU Marketplace MCP","mp","Wildberries, Ozon, Яндекс Маркет и др.","Одиннадцать маркетплейсов и Циан как MCP-серверы: WB, Ozon, Яндекс Маркет и др.",False,("manual",None),None),
("ilyautov/marketplaces-mcp-ru","marketplaces-ru","Marketplaces MCP RU","mp","Wildberries, Ozon, Яндекс Маркет, Авито","Кабинеты WB, Ozon, Яндекс Маркета и Авито: продажи, заказы, остатки.",False,("manual",None),None),
("eduard256/ozon-mcp-server","ozon-shop-eduard","Ozon (покупатель)","mp","Ozon","Поиск товаров Ozon, карточки, цены и доставка.",False,("manual",None),None),
("PCDCK/ozon-mcp","ozon-seller-pcdck","Ozon Seller MCP","mp","Ozon","Ozon Seller API и Performance API для ИИ-агента.",False,("manual",None),None),
("DeviceIngineering/ozon-mcp-server","ozon-seller-156","Ozon Seller (156 инструментов)","mp","Ozon","Цены, акции, реклама, заказы — 156 инструментов Ozon Seller & Performance API.",False,("manual",None),None),
("neosheps/ozon-shopping-mcp","ozon-shopping","Ozon Shopping","mp","Ozon","Неофициальный поиск товаров, цен и отзывов Ozon.",False,("manual",None),None),
("Alexander-Zhukov/ozon-mcp","ozon-buyer","Ozon (кабинет покупателя)","mp","Ozon","Заказы, история покупок, корзина и избранное покупателя Ozon.",False,("manual",None),None),
("DeviceIngineering/wb-mcp-server","wb-seller-197","Wildberries Seller (197 инструментов)","mp","Wildberries","197 инструментов Wildberries Seller API: цены, акции, реклама, заказы.",False,("manual",None),None),
("dmitriipolushin/wildberries-api-mcp-server","wb-api-dp","Wildberries API MCP","mp","Wildberries","Сервер для Wildberries API.",False,("manual",None),None),
("ilyautov/yandex-market-mcp-ru","yandex-market","Яндекс Маркет MCP","mp","Яндекс Маркет","API Яндекс Маркета: заказы, товары, цены, отчёты, отзывы.",False,("manual",None),None),
("dontsovcmc/mcp-server-yandex-market-seller","yandex-market-seller","Yandex Market Seller","mp","Яндекс Маркет","MCP-сервер для продавцов Яндекс Маркета.",False,("manual",None),None),
("elchin92/avito-mcp","avito-148","Avito MCP (148 инструментов)","mp","Авито","Чаты, объявления, заказы и аналитика Авито, режимы только для чтения.",False,("manual",None),None),
("ilyautov/avito-mcp-ru","avito-ru","Avito MCP RU","mp","Авито","API Авито: объявления, чаты, заказы, автозагрузка, отзывы.",False,("manual",None),None),
("icyberdeveloper/tbank-mcp","tbank","T-Bank MCP","bank","Т-Банк","Неофициальный сервер мобильного банка Т-Банк: счета, карты, операции.",False,("manual",None),None),
("viptdv333-boop/t-invest-tinkoff-mcp","t-invest","T-Invest MCP","bank","Т-Инвестиции","Сервер для T-Invest API (Тинькофф Инвестиции).",False,("manual",None),None),
("Sprytin/tinkoff-investments-mcp-server","tinkoff-investments-kt","Tinkoff Investments (Kotlin)","bank","Т-Инвестиции","MCP-сервер Т-Инвестиций на Kotlin.",False,("manual",None),None),
("ex3lite/sber-mcp","sber-online","SberBank Online MCP","bank","Сбербанк","Неофициальный сервер и SDK для СберБанк Онлайн: чтение данных, подтверждение человеком.",False,("manual",None),None),
("altrr2/yandex-tools-mcp","yandex-tools","Yandex Tools MCP","ya","Яндекс (разные API)","Набор инструментов для API Яндекса.",False,("manual",None),None),
("SvechaPVL/yandex-mcp","yandex-mcp-svecha","Yandex MCP","ya","Яндекс (разные API)","MCP-сервер для сервисов Яндекса.",False,("manual",None),None),
("aikts/yandex-tracker-mcp","yandex-tracker","Yandex Tracker MCP","ya","Яндекс Трекер","Задачи, очереди и поиск в Яндекс Трекере.",False,("uvx","yandex-tracker-mcp@latest"),None),
("n-r-w/yandex-mcp","yandex-tracker-wiki","Yandex Tracker & Wiki","ya","Яндекс Трекер / Вики","Сервер на Go для Яндекс Трекера и Вики.",False,("manual",None),None),
("best-doctor/mcp-yandex-wiki","yandex-wiki","Yandex Wiki MCP","ya","Яндекс Вики","Чтение и поиск страниц Яндекс Вики.",False,("manual",None),None),
("Dudude-bit/yandex-lavka-mcp","yandex-lavka","Яндекс Лавка","ya","Яндекс Лавка","Неофициальный заказ продуктов в Яндекс Лавке: поиск, корзина.",False,("manual",None),None),
("peschinskiy/yandex-maps-mcp","yandex-maps","Yandex Maps MCP","ya","Яндекс Карты","Рендеринг карт и геокодирование через API Яндекс Карт.",False,("manual",None),None),
("BoxLab-Ltd/yandex-metrica-mcp","yandex-metrika-boxlab","Yandex Metrica MCP","ads","Яндекс Метрика","Запросы к веб-аналитике Метрики на естественном языке.",False,("manual",None),None),
("atomkraft/yandex-metrika-mcp","yandex-metrika-atomkraft","Yandex Metrika MCP","ads","Яндекс Метрика","Отчёты и статистика Яндекс Метрики.",False,("manual",None),None),
("Yurich-ru/yandex-ads-mcp","yandex-ads","Yandex Ads MCP (152 инструмента)","ads","Яндекс Директ / Метрика / Wordstat","Директ, Метрика, Аудитории и Wordstat — 152 инструмента.",False,("manual",None),None),
("stufently/yandex-mcp","yandex-mcp-stufently","Yandex MCP (94 инструмента)","ads","Яндекс Поиск / Wordstat / Вебмастер / Метрика / Директ","Серверы для Поиска, Wordstat, Вебмастера, Метрики и Директа.",False,("manual",None),None),
("axisrow/yandex-direct-mcp-plugin","yandex-direct-plugin","Yandex Direct Plugin для Claude Code","ads","Яндекс Директ","Плагин Claude Code: MCP-сервер, скиллы и OAuth для Директа.",False,("manual",None),None),
("georgy-agaev/yandex-direct-metrica-mcp","yandex-direct-metrica","Yandex Direct + Metrica","ads","Яндекс Директ / Метрика","Директ, Метрика, Wordstat и Аудитории — режимы read-only и pro.",False,("manual",None),None),
("askads/mcp-yandex-direct","yandex-direct-askads","Yandex Direct MCP","ads","Яндекс Директ","Управление контекстной рекламой: кампании, ставки, объявления.",False,("manual",None),None),
("askads/mcp-yandex-wordstat","yandex-wordstat","Yandex Wordstat MCP","ads","Яндекс Wordstat","Частотность, похожие фразы и динамика запросов Wordstat.",False,("manual",None),None),
("weselow/Yandex-webmaster-mcp-server","yandex-webmaster","Yandex Webmaster MCP","ads","Яндекс Вебмастер","46 инструментов для Yandex Webmaster API v4.",False,("manual",None),None),
("gdigora/yandex-mail-mcp","yandex-mail","Yandex Mail MCP","ya","Яндекс Почта","Чтение, поиск и отправка писем Яндекс Почты через IMAP/SMTP.",False,("manual",None),None),
("Antiloop-git/yandex-disk-mcp","yandex-disk","Yandex Disk MCP","ya","Яндекс Диск","Управление файлами Яндекс Диска через REST API.",False,("manual",None),None),
("ADIKANT/datalens-dev-mcp","datalens","DataLens Dev MCP","ya","Yandex DataLens","Безопасная разработка дашбордов Yandex DataLens с ИИ.",False,("manual",None),None),
("ssubbotin/yandex-iot-mcp","yandex-smart-home","Умный дом Яндекса (Алиса)","ya","Яндекс Умный дом","Список и управление устройствами умного дома Яндекса, сценарии.",False,("manual",None),None),
("T1Trit/yandex-browser-mcp","yandex-browser","Yandex Browser MCP","ya","Яндекс Браузер","Управление вкладками Яндекс Браузера.",False,("manual",None),None),
("ilyautov/diadoc-mcp-ru","diadoc","Диадок MCP","acc","Контур.Диадок","API Диадока: документы и электронный документооборот (114 методов).",False,("manual",None),None),
("ilyautov/moysklad-mcp-ru","moysklad-ilyautov","МойСклад MCP","acc","МойСклад","Остатки, товары, заказы, документы и отчёты МойСклад.",False,("manual",None),None),
("luna-pulse/DaDataMcp","dadata","DaData MCP","biz","DaData","Локальный сервер DaData: подсказки, адреса, компании по ИНН.",False,("manual",None),None),
("AmplifyLab/elba-mcp","kontur-elba","Контур.Эльба MCP","acc","Контур.Эльба","Мост к публичному API Контур.Эльбы.",False,("manual",None),None),
("BuDum-Tss/ktalk-mcp","kontur-talk","Контур.Толк MCP","prod","Контур.Толк","Записи, транскрипты и саммари встреч Контур.Толк.",False,("manual",None),None),
("a-slvn/selectel-mcp","selectel","Selectel MCP","cloud","Selectel","Облако Selectel: OpenStack-серверы, S3, биллинг.",False,("manual",None),None),
("stufently/selectel-s3-mcp-ai-cli","selectel-s3","Selectel S3 MCP","cloud","Selectel S3","Сервер, CLI и скилл для объектного хранилища Selectel S3.",False,("manual",None),None),
("shodenis/Russian-Law-MCP","russian-law","Russian Law MCP","biz","Законодательство РФ","Поиск по федеральному законодательству России.",False,("manual",None),None),
("atomno-mcp/mcp-cbr-rates","cbr-rates","ЦБ РФ: курсы и ставки","bank","Банк России","Курсы ЦБ РФ, ключевая ставка, инфляция и макростатистика.",False,("manual",None),None),
("penmadebykisss/ru-business-mcp","ru-business","RU Business MCP","biz","ФНС / ЕГРЮЛ","Проверка компаний по ИНН (ЕГРЮЛ ФНС) и другие данные без токенов.",False,("manual",None),None),
("Aiyo28/yzel","yzel","Yzel","crm","1С, WB, Ozon, Битрикс24, amoCRM, МойСклад","Коннекторы для бизнес-инструментов СНГ: 1С, WB, Ozon, Битрикс24, amoCRM, МойСклад.",False,("manual",None),None),
("finmap-org/mcp-server","finmap","finmap.org","bank","Биржи (в т.ч. MOEX)","Исторические данные бирж США, Великобритании, России и др.",False,("manual",None),None),
]
WW=dict(amocrm=("crm","amoCRM"),aprovodka=("acc","1С:Предприятие"),avito=("mp","Авито"),bitrix24=("crm","Битрикс24"),boxberry=("log","Boxberry"),calltouch=("ads","Calltouch"),cbr=("bank","Банк России"),cdek=("log","СДЭК"),cloudpayments=("bank","CloudPayments"),**{"delovye-linii":("log","Деловые Линии")},elma365=("crm","ELMA365"),getcourse=("crm","GetCourse"),gigachat=("ai","GigaChat (Сбер)"),hh=("hr","HeadHunter"),huntflow=("hr","Huntflow"),**{"kontur-focus":("biz","Контур.Фокус"),"mango-office":("tel","Mango Office"),"mts-exolve":("tel","МТС Exolve"),"pochta-russia":("log","Почта России"),"vk-ads":("ads","VK Реклама"),"yandex-search":("ya","Yandex Search API / Wordstat"),"2gis":("log","2ГИС")},megaplan=("crm","Мегаплан"),mindbox=("crm","Mindbox"),moysklad=("acc","МойСклад"),planfix=("crm","Планфикс"),retailcrm=("crm","RetailCRM"),robokassa=("bank","Robokassa"),roistat=("ads","Roistat"),salutespeech=("ai","SaluteSpeech (Сбер)"),tilda=("web","Tilda"),tkassa=("bank","Т-Банк (Т-Касса)"),travelpayouts=("web","Travelpayouts"),unisender=("tel","UniSender"),wildberries=("mp","Wildberries"),yookassa=("bank","ЮKassa"),kaspi=("mp","Kaspi (Казахстан)"),payme=("bank","Payme (Узбекистан)"),cbu=("bank","ЦБ Узбекистана"))
import html
s=open('wwmcp.html').read(); wwdesc={}
for tr in re.findall(r'<tr>(.*?)</tr>',s,re.S):
    t=[html.unescape(re.sub('<[^>]+>','',x)).strip() for x in re.findall(r'<td[^>]*>(.*?)</td>',tr,re.S)]
    if len(t)>=3 and t[0].startswith('@theyahia/'): wwdesc[t[0]]=t[2]
def snippets(name,kind,val):
    key=name
    if kind in("npx","uvx"):
        cmd=kind; args=(["-y"] if kind=="npx" else [])+val.split()
        cfg={"mcpServers":{key:{"command":cmd,"args":args}}}
        cc=f"claude mcp add {key} -- {cmd} {' '.join(args)}"
        tr="stdio"
    elif kind=="docker":
        args=["run","-i","--rm",val]; cfg={"mcpServers":{key:{"command":"docker","args":args}}}
        cc=f"claude mcp add {key} -- docker {' '.join(args)}"; tr="stdio"
    elif kind=="http":
        cfg={"mcpServers":{key:{"url":val}}}; cc=f"claude mcp add --transport http {key} {val}"; tr="http"
    else: return None,None,None
    return cc,json.dumps(cfg,ensure_ascii=False,indent=2),tr
out=[]
def meta(repo):
    return m.get(repo.lower())
for repo,slug,name,cat,svc,desc,off,inst,sub in R:
    d=meta(repo)
    if not d: print("NO META",repo); continue
    cc,cur,tr=snippets(slug,*inst)
    out.append(dict(slug=slug,name=name,description_ru=desc,category=C[cat],service=svc,repo_url=("https://github.com/"+sub) if sub else d['html_url'],official=off,language=d.get('language'),license=(d.get('license') or {}).get('spdx_id'),stars=d['stargazers_count'],last_commit=d['pushed_at'][:10],transport=tr or "stdio",transport_verified=bool(tr),install={"claude_code":cc,"cursor":cur,"note":None if cc else "Установка из исходников — см. README репозитория."},yandex_ai_studio=("Подходит: удалённый HTTP-сервер можно подключить в Yandex AI Studio (MCP Hub)." if tr=="http" else None),gigacode=None,created_at=d.get('created_at','')[:10],source="github" ,monorepo=bool(sub)))
for repo,slug,cat,svc,desc in N:
    d=meta(repo)
    if not d: print('NO META',repo); continue
    out.append(dict(slug=slug,name=d['name'],description_ru=desc,category=C[cat],service=svc,repo_url=d['html_url'],official=repo in OFF,language=d.get('language'),license=(d.get('license') or {}).get('spdx_id'),stars=d['stargazers_count'],last_commit=d['pushed_at'][:10],transport='stdio',transport_verified=False,install={'claude_code':None,'cursor':None,'note':'Установка из исходников — см. README репозитория.'},yandex_ai_studio=None,gigacode=None,created_at=d.get('created_at','')[:10],source='github',monorepo=False))
yc=meta('yandex-cloud/mcp')
for k,dirn,nm,desc in [('toolkit','toolkit','Toolkit','Управление Compute, VPC, IAM, Object Storage и YDB (42 инструмента).'),('docs','documentation','Documentation','Поиск и навигация по документации Yandex Cloud.'),('search','search','Search','Классический и генеративный веб-поиск через Yandex Search API.'),('functions','functions','Cloud Functions','Управление Cloud Functions (serverless).'),('containers','containers','Serverless Containers','Управление Serverless Containers.'),('triggers','triggers','Triggers','Триггеры для Cloud Functions и Serverless Containers.'),('workflows','workflows','Workflows','Управление Yandex Cloud Workflows.'),('apigateway','apigateway','API Gateway','Управление API Gateway.'),('mcpgateway','mcpgateway','MCP Gateway','Настройка MCP-шлюзов с собственными инструментами (preview).'),('datacatalog-consumer','datacatalog-consumer','Data Catalog','Поиск таблиц и графов зависимостей в Data Catalog.')]:
    url=f'https://{k}.mcp.cloud.yandex.net/mcp'; key='yandex-cloud-'+k
    out.append(dict(slug=key,name='Yandex Cloud '+nm+' MCP',description_ru=desc+' Официальный сервер Yandex Cloud, доступен в Yandex Cloud Marketplace.',category=C['cloud'],service='Yandex Cloud',repo_url=f'https://github.com/yandex-cloud/mcp/tree/master/servers/{dirn}-mcp-server',official=True,language='TypeScript',license='Apache-2.0',stars=yc['stargazers_count'],last_commit=yc['pushed_at'][:10],transport='http',transport_verified=True,install={'claude_code':f'claude mcp add --transport http {key} {url} --header "Authorization: Bearer <IAM_TOKEN>"','cursor':json.dumps({'mcpServers':{key:{'command':'npx','args':['-y','@yandex-cloud/mcp','-s',k]}}},indent=2),'note':'Удалённый сервер требует IAM-токен; локальный вариант — npm-пакет @yandex-cloud/mcp (-s '+k+'). Можно развернуть из Yandex Cloud Marketplace.'},yandex_ai_studio='Подключается в AI Studio → Agent Core → MCP-серверы (из Yandex Cloud Marketplace).',gigacode=None,created_at=yc.get('created_at','')[:10],source='yandex.cloud/marketplace',monorepo=True))
ww=meta("theYahia/WWmcp")
for k,(cat,svc) in WW.items():
    pkg="@theyahia/aprovodka" if k=="aprovodka" else f"@theyahia/{k}-mcp"
    cc,cur,tr=snippets(k,"npx",pkg)
    out.append(dict(slug="wwmcp-"+k,name=f"{svc} (WWmcp)",description_ru=wwdesc.get(pkg,""),category=C[cat],service=svc,repo_url=f"https://github.com/theYahia/WWmcp/tree/main/servers/{k}",official=False,language="TypeScript",license="MIT",stars=ww['stargazers_count'],last_commit=ww['pushed_at'][:10],transport="stdio",transport_verified=True,install={"claude_code":cc,"cursor":cur,"note":f"npm-пакет {pkg}; ключи API передаются через env (см. README)."},yandex_ai_studio=None,gigacode=None,created_at=ww['created_at'][:10],source="theyahia.github.io/WWmcp",monorepo=True))
for e in out: e["gigacode"]="GigaCode поддерживает MCP через стандартный JSON-конфиг mcpServers — совместимость не проверялась." if e["install"]["cursor"] else None
assert len({e['slug'] for e in out})==len(out)
json.dump(out,open('../data/servers.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
print(len(out)); print(Counter(e['category'] for e in out).most_common())
