import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from datetime import datetime

TOKEN = "7936516818:AAGNQ3hrr_AiGv2W1FvLd52OKhrHEbxjy4k"
EXCHANGE_API_KEY = "30436212afa73690f74a4f4b"  # Замените на ваш ключ API от exchangerate-api.com

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

async def get_usd_rub_rate():
    """Получение актуального курса USD к RUB."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD") as response:
                if response.status == 200:
                    data = await response.json()
                    rate = data["conversion_rates"]["RUB"]
                    return rate
                else:
                    return None
    except Exception:
        return None

async def get_usd_kzt_rate():
    """Получение актуального курса USD к KZT."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/latest/USD") as response:
                if response.status == 200:
                    data = await response.json()
                    rate = data["conversion_rates"]["KZT"]
                    return rate
                else:
                    return None
    except Exception:
        return None

# Клавиатура выбора языка при старте
language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇷🇺 RUS"),
            KeyboardButton(text="🇬🇧 ENG"),
            KeyboardButton(text="🇯🇵 JPN"),
            KeyboardButton(text="🇨🇳 CHN"),
            KeyboardButton(text="🇰🇿 KAZ")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Инлайн-клавиатура для Instagram и Telegram
social_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Instagram", url="https://www.instagram.com/odeolab?igsh=MTFha2k3eGVrOWFncw%3D%3D&utm_source=qr"),
            InlineKeyboardButton(text="Telegram", url="https://t.me/ODEOlab1")
        ]
    ]
)

# Кнопка переключения языка для главного меню
switch_language_button = KeyboardButton(text="🌐 Сменить язык / Change Language / 言語を変更 / 更换语言 / Тілді ауыстыру")

# Главное меню на русском
main_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ О нас")],
        [KeyboardButton(text="📋 Перечень услуг")],
        [KeyboardButton(text="☎️ Связь с менеджером")],
        [KeyboardButton(text="💰 Оплата")],
        [switch_language_button]
    ],
    resize_keyboard=True
)

# Клавиатура для раздела "О нас" на русском
about_us_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📑 Документальная база")],
        [KeyboardButton(text="💻 Цифровые консультанты")],
        [KeyboardButton(text="👥 Эксперты")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

# Главное меню на английском
main_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ About Us")],
        [KeyboardButton(text="📋 Services List")],
        [KeyboardButton(text="☎️ Contact Manager")],
        [KeyboardButton(text="💰 Payment")],
        [switch_language_button]
    ],
    resize_keyboard=True
)

# Клавиатура для раздела "О нас" на английском
about_us_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📑 Documentation Base")],
        [KeyboardButton(text="💻 Digital Consultants")],
        [KeyboardButton(text="👥 Experts")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)

# Главное меню на японском
main_keyboard_jp = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ 私たちについて")],
        [KeyboardButton(text="📋 サービス一覧")],
        [KeyboardButton(text="☎️ マネージャーに連絡")],
        [KeyboardButton(text="💰 支払い")],
        [switch_language_button]
    ],
    resize_keyboard=True
)

# Клавиатура для раздела "О нас" на японском
about_us_keyboard_jp = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📑 ドキュメントベース")],
        [KeyboardButton(text="💻 デジタルコンサルタント")],
        [KeyboardButton(text="👥 専門家")],
        [KeyboardButton(text="⬅️ 戻る")]
    ],
    resize_keyboard=True
)

# Главное меню на китайском
main_keyboard_cn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ 关于我们")],
        [KeyboardButton(text="📋 服务列表")],
        [KeyboardButton(text="☎️ 联系经理")],
        [KeyboardButton(text="💰 付款")],
        [switch_language_button]
    ],
    resize_keyboard=True
)

# Клавиатура для раздела "О нас" на китайском
about_us_keyboard_cn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📑 文档库")],
        [KeyboardButton(text="💻 数字顾问")],
        [KeyboardButton(text="👥 专家")],
        [KeyboardButton(text="⬅️ 返回")]
    ],
    resize_keyboard=True
)

# Главное меню на казахском
main_keyboard_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="❓ Біз туралы")],
        [KeyboardButton(text="📋 Қызметтер тізімі")],
        [KeyboardButton(text="☎️ Менеджермен байланыс")],
        [KeyboardButton(text="💰 Төлем")],
        [switch_language_button]
    ],
    resize_keyboard=True
)

# Клавиатура для раздела "О нас" на казахском
about_us_keyboard_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📑 Құжаттық базасы")],
        [KeyboardButton(text="💻 Цифрлық кеңесшілер")],
        [KeyboardButton(text="👥 Сарапшылар")],
        [KeyboardButton(text="⬅️ Артқа")]
    ],
    resize_keyboard=True
)

# Клавиатуры услуг на разных языках
services_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 Профориентация")],
        [KeyboardButton(text="🧠 Анализ личности")],
        [KeyboardButton(text="🌟 Сфера самореализации")],
        [KeyboardButton(text="🧩 Распаковка бизнеса/компании/организации/карьеры")],
        [KeyboardButton(text="🎁 Бесплатная консультация")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

services_keyboard_en = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 Career Guidance")],
        [KeyboardButton(text="🧠 Personality Analysis")],
        [KeyboardButton(text="🌟 Sphere of Self-Realization")],
        [KeyboardButton(text="🧩 Business/Company/Career Analysis")],
        [KeyboardButton(text="🎁 Free Consultation")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)

services_keyboard_jp = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 キャリアガイダンス")],
        [KeyboardButton(text="🧠 性格分析")],
        [KeyboardButton(text="🌟 自己実現の分野")],
        [KeyboardButton(text="🧩 ビジネス/会社/キャリア分析")],
        [KeyboardButton(text="🎁 無料相談")],
        [KeyboardButton(text="⬅️ 戻る")]
    ],
    resize_keyboard=True
)

services_keyboard_cn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 职业指导")],
        [KeyboardButton(text="🧠 性格分析")],
        [KeyboardButton(text="🌟 自我实现领域")],
        [KeyboardButton(text="🧩 业务/公司/职业分析")],
        [KeyboardButton(text="🎁 免费咨询")],
        [KeyboardButton(text="⬅️ 返回")]
    ],
    resize_keyboard=True
)

services_keyboard_kz = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎯 Кәсіби бағдар")],
        [KeyboardButton(text="🧠 Тұлға талдауы")],
        [KeyboardButton(text="🌟 Өзін-өзі жүзеге асыру саласы")],
        [KeyboardButton(text="🧩 Бизнес/компания/ұйым/мансап талдауы")],
        [KeyboardButton(text="🎁 Тегін кеңес")],
        [KeyboardButton(text="⬅️ Артқа")]
    ],
    resize_keyboard=True
)

# Словарь для хранения языка пользователя
user_language = {}

@dp.message(F.text.lower() == "/start")
async def start_handler(message: Message):
    await message.answer(
        "Выберите язык",
        reply_markup=language_keyboard
    )

@dp.message(F.text.in_({"🇷🇺 RUS", "🇬🇧 ENG", "🇯🇵 JPN", "🇨🇳 CHN", "🇰🇿 KAZ"}))
async def language_chosen(message: Message):
    user_id = message.from_user.id
    text = message.text
    if text == "🇷🇺 RUS":
        user_language[user_id] = "ru"
        await message.answer(
            "Мы — команда цифровых консультантов и экспертов в сфере личностного роста и бизнеса «ODEOlab»\n\n"
            "У нас есть рабочий алгоритм действий, следуя которому, вы повысите эффективность, увидите новые точки роста, решите бизнес-задачи\n\n"
            "Готовы начать?",
            reply_markup=social_keyboard
        )
        await message.answer(
            "Выберите действие:",
            reply_markup=main_keyboard_ru
        )
    elif text == "🇬🇧 ENG":
        user_language[user_id] = "en"
        await message.answer(
            "We are a team of digital consultants and experts in personal growth and business at «ODEOlab»\n\n"
            "We have a working action algorithm that, when followed, will help you boost efficiency, identify new growth opportunities, and solve business challenges\n\n"
            "Ready to start?",
            reply_markup=social_keyboard
        )
        await message.answer(
            "Choose an action:",
            reply_markup=main_keyboard_en
        )
    elif text == "🇯🇵 JPN":
        user_language[user_id] = "jp"
        await message.answer(
            "私たちは「ODEOlab」のパーソナル成長とビジネスの分野におけるデジタルコンサルタントおよび専門家のチームです\n\n"
            "私たちは効率を高め、新しい成長の機会を見つけ、ビジネス課題を解決するのに役立つ実践的な行動アルゴリズムを持っています\n\n"
            "始めますか？",
            reply_markup=social_keyboard
        )
        await message.answer(
            "アクションを選択してください：",
            reply_markup=main_keyboard_jp
        )
    elif text == "🇨🇳 CHN":
        user_language[user_id] = "cn"
        await message.answer(
            "我们是「ODEOlab」的数字顾问团队，专注于个人成长和商业领域\n\n"
            "我们拥有一个实用的行动算法，遵循它将帮助您提升效率，找到新的增长点，并解决商业挑战\n\n"
            "准备开始了吗？",
            reply_markup=social_keyboard
        )
        await message.answer(
            "选择一个操作：",
            reply_markup=main_keyboard_cn
        )
    elif text == "🇰🇿 KAZ":
        user_language[user_id] = "kz"
        await message.answer(
            "Біз — «ODEOlab» командасы, жеке өсу және бизнес саласындағы цифрлық кеңесшілер мен сарапшылармыз\n\n"
            "Бізде тиімділікті арттыруға, жаңа өсу нүктелерін көруге және бизнес міндеттерін шешуге көмектесетін нақты іс-қимыл алгоритмі бар\n\n"
            "Бастауға дайынсыз ба?",
            reply_markup=social_keyboard
        )
        await message.answer(
            "Әрекетті таңдаңыз:",
            reply_markup=main_keyboard_kz
        )

@dp.message()
async def main_menu_handler(message: Message):
    user_id = message.from_user.id
    lang = user_language.get(user_id, "ru")
    text = message.text
    # Получение курсов валют
    usd_rub_rate = await get_usd_rub_rate()
    usd_kzt_rate = await get_usd_kzt_rate()
    rate_text = (
        f"Актуальный курс: 1$ = {usd_rub_rate:.2f}₽ (по данным на {datetime.now().strftime('%d.%m.%Y')})"
        if usd_rub_rate
        else "Курс валют временно недоступен."
    ) if lang != "kz" else (
        f"Актуалды курс: 1$ = {usd_kzt_rate:.2f}₸ (деректер бойынша {datetime.now().strftime('%d.%m.%Y')})"
        if usd_kzt_rate
        else "Валюта курсы уақытша қолжетімсіз."
    )

    # Кнопка смены языка
    if text == "🌐 Сменить язык / Change Language / 言語を変更 / 更换语言 / Тілді ауыстыру":
        await message.answer(
            "Выберите язык",
            reply_markup=language_keyboard
        )
        return

    # Русский
    if lang == "ru":
        if text == "📋 Перечень услуг":
            await message.answer("Выберите интересующую услугу:", reply_markup=services_keyboard_ru)
        elif text == "⬅️ Назад":
            await message.answer("Возврат в главное меню.", reply_markup=main_keyboard_ru)
        elif text == "🎯 Профориентация":
            await message.answer(
                "Профориентация — поможет вам определить сильные стороны, интересы и ценности человека, чтобы найти ту сферу, в которой можно преуспеть, почувствовать вдохновение.\n\n"
                "- В какой сфере мне будет максимально комфортно и интересно работать?\n"
                "- Где я смогу реализовать свои навыки и чувствовать себя на своем месте?\n"
                "- В какой сфере или окружении мне стоит искать работу, чтобы чувствовать вдохновение и развитие?\n"
                "- Как выбрать наиболее подходящую для меня профессиональную среду?\n\n"
                f"Продолжительность 45 минут\n\n"
                f"Стоимость 3300₽/42$\n\n{rate_text}"
            )
        elif text == "🧠 Анализ личности":
            await message.answer(
                "Когда вы понимаете себя, свою ценность, на чем построена ваша ценность, вы увидите в чем ваша слабость.\n\n"
                "Четкое понимание своей природы это не только о карьере и профессиональных целях, но и о деньгах.\n\n"
                f"Продолжительность 90 минут\n\n"
                f"Стоимость 8700₽/105$"
            )
        elif text == "🌟 Сфера самореализации":
            await message.answer(
                "Самореализация - это реализация потенциала личности, осуществление своего человеческого назначения, призвания.\n\n"
                "Позвольте задать вам вопрос?\n\n"
                "Совпадаете ли вы со своей профориентацией, т.е со сферой своей деятельности, находитесь ли вы, на своем месте?\n\n"
                "Мы покажем вам, как работает схема\n\n"
                "Вы в своей сфере реализации = деньги\n\n"
                f"Продолжительность 3 сессии по 45 минут\n\n"
                f"1 сессия - разбор типа личности\n"
                f"2 сессия - определение навыков (soft skills, hard skills, meta skills)\n"
                f"3 сессия - пошаговая инструкция карьерного или бизнес плана согласно вашего запроса\n\n"
                f"Стоимость 15000₽/186$"
            )
        elif text == "🧩 Распаковка бизнеса/компании/организации/карьеры":
            await message.answer(
                "Распаковка бизнеса — это как искать сокровища в большом сундуке: нужно правильно определить, где лежит главный клад!\n\n"
                "Это процесс глубокого анализа и понимания всех составляющих, определение слабых мест вашего дела, а главное внутренних ресурсов (сотрудников).\n\n"
                "Это взгляд со стороны, некоторое подсвечивание.\n"
                "В итоге, ваш бизнес становится не просто понятнее, а действительно мощной машиной для достижения целей!\n\n"
                f"Продолжительность 3 - 6 месяцев\n\n"
                f"Стоимость 330000₽/4200$\n\n{rate_text}"
            )
        elif text == "🎁 Бесплатная консультация":
            await message.answer(
                "Наша консультация поможет Вам понять наш профессионализм и почувствовать доверие.\n\n"
                "Подготовьте три особо важных для вас вопроса.\n\n"
                "Возможно это:\n"
                "- отношения\n"
                "- лучшая дата для заключения брака\n"
                "- денежный код\n"
                "- в чем выше вдохновение\n"
                "- сексуальный партнер\n"
                "и т. д.\n\n"
                "Тогда консультация будет более емкой и полезной.\n\n"
                "Продолжительность 15 минут"
            )
        elif text == "☎️ Связь с менеджером":
            await message.answer(
                "Связь с менеджером\n\n"
                "Телеграмм: @ODEOlab\n\n"
                "📞 +79263454503"
            )
        elif text == "❓ О нас":
            await message.answer("Узнайте больше о нас:", reply_markup=about_us_keyboard_ru)
        elif text == "💰 Оплата":
            await message.answer(
                "Оплата принимается удобными для вас способами.\n\n"
                "Свяжитесь с менеджером для деталей.\n\n"
                "@ODEOlab"
            )
        elif text == "💻 Цифровые консультанты":
            await message.answer(
                "Оксана Никитина\n\n"
                "Учредитель международной консалтинговой ассоциации ODEO lab\n\n"
                "Практикующий цифровой консультант личностного роста и бизнеса SYUCAI TRAINING INSTITUTE Дубай 🇦🇪 более 6 лет\n\n"
                "Куратор цифровых консультантов по Уральскому Федеральному Округу\n\n"
                "Руководитель клуба г. Тюмень"
            )
        elif text == "👥 Эксперты":
            await message.answer(
                "<b>Елена Турлак</b>\n\n"
                "Аналитик и управленец в сфере логистики и торговли\n\n"
                "Опыт ведения сетевого и классического бизнеса более 20 лет\n\n"
                "<b>Динара Сафина</b>\n\n"
                "Юрист международного уровня\n\n"
                "Более 19 лет опыта в сфере юридического консалтинга и аудита в различных юрисдикциях стран РФ,ЕС, ОАЭ (регистрации компаний, сопровождение бизнеса компаний)\n\n"
                "Частная юридическая практика более 5 лет (более 1000 выигрышных судебных заседаний)"
            )
        elif text == "📑 Документальная база":
            await message.answer(
                "Официальные документы, лицензии, сертификаты\n\n"
                "https://t.me/ODEOlab1"
            )
        elif text in ["📑 Документальная база", "💻 Цифровые консультанты", "👥 Эксперты", "⬅️ Назад"]:
            if text == "⬅️ Назад":
                await message.answer("Возврат в главное меню.", reply_markup=main_keyboard_ru)
            else:
                await message.answer("Информация пока в разработке.")
        else:
            await message.answer("Пожалуйста, выберите пункт меню.")

    # Английский
    elif lang == "en":
        if text == "📋 Services List":
            await message.answer("Please choose a service:", reply_markup=services_keyboard_en)
        elif text == "⬅️ Back":
            await message.answer("Returning to main menu.", reply_markup=main_keyboard_en)
        elif text == "🎯 Career Guidance":
            await message.answer(
                "Career guidance — helps determine a person's strengths, interests, and values to find the field where they can succeed and feel inspired.\n\n"
                "- In which field will I feel most comfortable and interested in working?\n"
                "- Where can I apply my skills and feel in my element?\n"
                "- In what field or environment should I look for a job to feel inspired and grow?\n"
                "- How can I choose the most suitable professional environment for myself?\n\n"
                f"<b>Duration: 45 minutes\n\n"
                f"Cost: 3300₽/42$\n\n{rate_text}</b>"
            )
        elif text == "🧠 Personality Analysis":
            await message.answer(
                "When you understand yourself, your value, and what your value is built upon, you will see your weaknesses.\n\n"
                "A clear understanding of your nature is not only about career and professional goals but also about money.\n\n"
                f"Duration: 90 minutes\n\n"
                f"Cost: 8700₽/105$"
            )
        elif text == "🌟 Sphere of Self-Realization":
            await message.answer(
                "Self-realization is the realization of a person's potential, the fulfillment of their human destiny and calling.\n\n"
                "Allow us to ask you a question?\n\n"
                "Are you aligned with your career guidance, i.e., with your field of activity, are you in your element?\n\n"
                "We will show you how the scheme works:\n\n"
                "You in your sphere of realization = money\n\n"
                f"Duration: 3 sessions of 45 minutes each\n\n"
                f"Session 1 - Personality analysis\n"
                f"Session 2 - Skills assessment (soft skills, hard skills, meta skills)\n"
                f"Session 3 - Step-by-step career or business plan based on your request\n\n"
                f"Cost: 15000₽/186$"
            )
        elif text == "🧩 Business/Company/Career Analysis":
            await message.answer(
                "Business analysis — is like searching for treasure in a big chest: you need to correctly identify where the main treasure lies!\n\n"
                "This is a process of deep analysis and understanding of all components, identifying the weaknesses of your business, and, most importantly, internal resources (employees).\n\n"
                "It’s an outside perspective that sheds light on your operations.\n"
                "Ultimately, your business becomes not only clearer but also a truly powerful machine for achieving goals!\n\n"
                f"<b>Duration: 3 - 6 months\n\n"
                f"Cost: 330000₽/4200$\n\n{rate_text}</b>"
            )
        elif text == "🎁 Free Consultation":
            await message.answer(
                "Our consultation will help you understand our professionalism and build trust.\n\n"
                "Prepare three particularly important questions for you.\n\n"
                "Possibly these:\n"
                "- relationships\n"
                "- best date for marriage\n"
                "- money code\n"
                "- where you find the most inspiration\n"
                "- sexual partner\n"
                "and so on.\n\n"
                "Then the consultation will be more comprehensive and useful.\n\n"
                "Duration: 15 minutes"
            )
        elif text == "☎️ Contact Manager":
            await message.answer(
                "Contact Manager\n\n"
                "Telegram: @ODEOlab\n\n"
                "📞 +79263454503"
            )
        elif text == "❓ About Us":
            await message.answer("Learn more about us:", reply_markup=about_us_keyboard_en)
        elif text == "💰 Payment":
            await message.answer(
                "Payment is accepted in ways convenient for you.\n\n"
                "Contact the manager for details.\n\n"
                "@ODEOlab"
            )
        elif text == "💻 Digital Consultants":
            await message.answer(
                "Oksana Nikitina\n\n"
                "Founder of the international consulting association ODEO lab\n\n"
                "Practicing digital consultant for personal growth and business at SYUCAI TRAINING INSTITUTE, Dubai 🇦🇪 for over 6 years\n\n"
                "Curator of digital consultants in the Ural Federal District\n\n"
                "Head of the club in Tyumen"
            )
        elif text == "👥 Experts":
            await message.answer(
                "<b>Elena Turlak</b>\n\n"
                "Analyst and manager in logistics and trade\n\n"
                "Over 20 years of experience in network and traditional business\n\n"
                "<b>Dinara Safina</b>\n\n"
                "International-level lawyer\n\n"
                "Over 19 years of experience in legal consulting and auditing across jurisdictions in Russia, EU, UAE (company registrations, business support)\n\n"
                "Private legal practice for over 5 years (over 1000 successful court cases)"
            )
        elif text == "📑 Documentation Base":
            await message.answer(
                "Official documents, licenses, certificates\n\n"
                "https://t.me/ODEOlab1"
            )
        elif text in ["📑 Documentation Base", "💻 Digital Consultants", "👥 Experts", "⬅️ Back"]:
            if text == "⬅️ Back":
                await message.answer("Returning to main menu.", reply_markup=main_keyboard_en)
            else:
                await message.answer("Information is under development.")
        else:
            await message.answer("Please select a menu option.")

    # Японский
    elif lang == "jp":
        if text == "📋 サービス一覧":
            await message.answer("サービスを選択してください:", reply_markup=services_keyboard_jp)
        elif text == "⬅️ 戻る":
            await message.answer("メインメニューに戻ります。", reply_markup=main_keyboard_jp)
        elif text == "🎯 キャリアガイダンス":
            await message.answer(
                "キャリアガイダンス — 人の強み、興味、価値観を特定し、成功し、インスピレーションを感じられる分野を見つけるのに役立ちます。\n\n"
                "- どの分野で最も快適に、興味を持って働けるか？\n"
                "- どこで自分のスキルを活かし、自分に合った場所だと感じられるか？\n"
                "- インスピレーションと成長を感じられる分野や環境で仕事を探すべきか？\n"
                "- 自分に最も適した職業環境を選ぶには？\n\n"
                f"<b>所要時間: 45分\n\n"
                f"費用: 3300₽/42$\n\n{rate_text}</b>"
            )
        elif text == "🧠 性格分析":
            await message.answer(
                "自分自身、自身の価値、そしてその価値が何に基づいているかを理解することで、あなたの弱点が見えてきます。\n\n"
                "自分の本質を明確に理解することは、キャリアやプロフェッショナルな目標だけでなく、お金にも関わります。\n\n"
                f"所要時間: 90分\n\n"
                f"費用: 8700₽/105$"
            )
        elif text == "🌟 自己実現の分野":
            await message.answer(
                "自己実現とは個人の潜在能力を実現し、人間としての使命や天職を果たすことです。\n\n"
                "質問させてください。\n\n"
                "あなたのキャリアガイダンス、つまり活動分野と一致していますか？あなたは自分の居場所にいるのでしょうか？\n\n"
                "私たちはこのスキームがどのように機能するかを示します。\n\n"
                "あなたが自己実現の分野にいれば = お金\n\n"
                f"所要時間: 45分のセッション3回\n\n"
                f"セッション1 - 性格分析\n"
                f"セッション2 - スキル評価（ソフトスキル、ハードスキル、メタスキル）\n"
                f"セッション3 - 要望に基づくキャリアまたはビジネスプランのステップごとの指示\n\n"
                f"費用: 15000₽/186$"
            )
        elif text == "🧩 ビジネス/会社/キャリア分析":
            await message.answer(
                "ビジネス分析 — 大きな宝箱の中で宝物を探すようなものです：主な宝物がどこにあるかを正しく特定する必要があります！\n\n"
                "これは、すべての構成要素を深く分析し理解するプロセスであり、あなたのビジネスの弱点を特定し、最も重要な内部リソース（従業員）を活用します。\n\n"
                "それは外部からの視点であり、ある種の光を当てることです。\n"
                "最終的に、あなたのビジネスは単に明確になるだけでなく、目標達成のための本当に強力なマシンになります！\n\n"
                f"<b>所要時間: 3 - 6ヶ月\n\n"
                f"費用: 330000₽/4200$\n\n{rate_text}</b>"
            )
        elif text == "🎁 無料相談":
            await message.answer(
                "私たちの相談は、プロフェッショナリズムを理解し、信頼を感じるお手伝いをします。\n\n"
                "特にあなたにとって重要な3つの質問を準備してください。\n\n"
                "例えば以下のようなもの:\n"
                "- 関係性\n"
                "- 結婚に最適な日\n"
                "- お金のコード\n"
                "- 最もインスピレーションを感じる場所\n"
                "- 性的パートナー\n"
                "など。\n\n"
                "そうすれば、相談がより包括的で役立つものになります。\n\n"
                "所要時間: 15分"
            )
        elif text == "☎️ マネージャーに連絡":
            await message.answer(
                "Contact Manager\n\n"
                "Telegram: @ODEOlab\n\n"
                "📞 +79263454503"
            )
        elif text == "❓ 私たちについて":
            await message.answer("Learn more about us:", reply_markup=about_us_keyboard_jp)
        elif text == "💰 支払い":
            await message.answer(
                "Payment is accepted in ways convenient for you.\n\n"
                "Contact the manager for details.\n\n"
                "@ODEOlab"
            )
        elif text == "💻 デジタルコンサルタント":
            await message.answer(
                "Oksana Nikitina\n\n"
                "Founder of the international consulting association ODEO lab\n\n"
                "Practicing digital consultant for personal growth and business at SYUCAI TRAINING INSTITUTE, Dubai 🇦🇪 for over 6 years\n\n"
                "Curator of digital consultants in the Ural Federal District\n\n"
                "Head of the club in Tyumen"
            )
        elif text == "👥 専門家":
            await message.answer(
                "<b>Elena Turlak</b>\n\n"
                "Analyst and manager in logistics and trade\n\n"
                "Over 20 years of experience in network and traditional business\n\n"
                "<b>Dinara Safina</b>\n\n"
                "International-level lawyer\n\n"
                "Over 19 years of experience in legal consulting and auditing across jurisdictions in Russia, EU, UAE (company registrations, business support)\n\n"
                "Private legal practice for over 5 years (over 1000 successful court cases)"
            )
        elif text == "📑 ドキュメントベース":
            await message.answer(
                "Official documents, licenses, certificates\n\n"
                "https://t.me/ODEOlab1"
            )
        elif text in ["📑 ドキュメントベース", "💻 デジタルコンサルタント", "👥 専門家", "⬅️ 戻る"]:
            if text == "⬅️ 戻る":
                await message.answer("メインメニューに戻ります。", reply_markup=main_keyboard_jp)
            else:
                await message.answer("情報は現在開発中です。")
        else:
            await message.answer("メニューから項目を選択してください。")

    # Китайский
    elif lang == "cn":
        if text == "📋 服务列表":
            await message.answer("请选择服务:", reply_markup=services_keyboard_cn)
        elif text == "⬅️ 返回":
            await message.answer("返回主菜单。", reply_markup=main_keyboard_cn)
        elif text == "🎯 职业指导":
            await message.answer(
                "职业指导 — 帮助您确定一个人的优势、兴趣和价值观，以找到能够成功并感受到激励的领域。\n\n"
                "- 在哪个领域我会感到最舒适和有趣？\n"
                "- 在哪里我能发挥我的技能并感到得心应手？\n"
                "- 在哪个领域或环境中我应该寻找工作以获得启发和发展？\n"
                "- 如何选择最适合我的职业环境？\n\n"
                f"<b>时长: 45分钟\n\n"
                f"费用: 3300₽/42$\n\n{rate_text}</b>"
            )
        elif text == "🧠 性格分析":
            await message.answer(
                "当你了解自己、自己的价值以及你的价值建立在何处时，你会看到自己的弱点。\n\n"
                "清晰地理解自己的本质不仅与职业和专业目标有关，也与金钱有关。\n\n"
                f"时长: 90分钟\n\n"
                f"费用: 8700₽/105$"
            )
        elif text == "🌟 自我实现领域":
            await message.answer(
                "自我实现是实现个人潜能，履行人类使命和天职的过程。\n\n"
                "请允许我们问您一个问题？\n\n"
                "您是否与您的职业指导一致，也就是说，与您的活动领域一致，您是否处于自己的位置？\n\n"
                "我们将向您展示这个方案如何运作：\n\n"
                "您在自己的实现领域 = 钱\n\n"
                f"时长: 3次45分钟的会话\n\n"
                f"第一次会话 - 性格分析\n"
                f"第二次会话 - 技能评估（软技能、硬技能、元技能）\n"
                f"第三次会话 - 根据您的需求制定职业或商业计划的逐步指导\n\n"
                f"费用: 15000₽/186$"
            )
        elif text == "🧩 业务/公司/职业分析":
            await message.answer(
                "业务分析 — 就像在大箱子里寻找宝藏：需要正确识别主要宝藏所在的位置！\n\n"
                "这是一个深入分析和理解所有组成部分的过程，识别你业务的弱点，并最重要的是内部资源（员工）。\n\n"
                "这是一种外部视角，带来一些启发性洞察。\n"
                "最终，你的业务不仅变得更清晰，还能成为实现目标的真正强大机器！\n\n"
                f"<b>时长: 3 - 6个月\n\n"
                f"费用: 330000₽/4200$\n\n{rate_text}</b>"
            )
        elif text == "🎁 免费咨询":
            await message.answer(
                "我们的咨询将帮助您了解我们的专业性并建立信任。\n\n"
                "请准备三个对您特别重要的提问。\n\n"
                "可能是以下内容：\n"
                "- 关系\n"
                "- 最佳结婚日期\n"
                "- 财富密码\n"
                "- 哪里最能激发灵感\n"
                "- 性伴侣\n"
                "等等。\n\n"
                "这样咨询将更全面且实用。\n\n"
                "时长: 15分钟"
            )
        elif text == "☎️ 联系经理":
            await message.answer(
                "Contact Manager\n\n"
                "Telegram: @ODEOlab\n\n"
                "📞 +79263454503"
            )
        elif text == "❓ 关于我们":
            await message.answer("Learn more about us:", reply_markup=about_us_keyboard_cn)
        elif text == "💰 付款":
            await message.answer(
                "Payment is accepted in ways convenient for you.\n\n"
                "Contact the manager for details.\n\n"
                "@ODEOlab"
            )
        elif text == "💻 数字顾问":
            await message.answer(
                "Oksana Nikitina\n\n"
                "Founder of the international consulting association ODEO lab\n\n"
                "Practicing digital consultant for personal growth and business at SYUCAI TRAINING INSTITUTE, Dubai 🇦🇪 for over 6 years\n\n"
                "Curator of digital consultants in the Ural Federal District\n\n"
                "Head of the club in Tyumen"
            )
        elif text == "👥 专家":
            await message.answer(
                "<b>Elena Turlak</b>\n\n"
                "Analyst and manager in logistics and trade\n\n"
                "Over 20 years of experience in network and traditional business\n\n"
                "<b>Dinara Safina</b>\n\n"
                "International-level lawyer\n\n"
                "Over 19 years of experience in legal consulting and auditing across jurisdictions in Russia, EU, UAE (company registrations, business support)\n\n"
                "Private legal practice for over 5 years (over 1000 successful court cases)"
            )
        elif text == "📑 文档库":
            await message.answer(
                "Official documents, licenses, certificates\n\n"
                "https://t.me/ODEOlab1"
            )
        elif text in ["📑 文档库", "💻 数字顾问", "👥 专家", "⬅️ 返回"]:
            if text == "⬅️ 返回":
                await message.answer("返回主菜单。", reply_markup=main_keyboard_cn)
            else:
                await message.answer("信息正在开发中。")
        else:
            await message.answer("请选择菜单项。")

    # Казахский
    elif lang == "kz":
        if text == "📋 Қызметтер тізімі":
            await message.answer("Қызығушылық тудыратын қызметті таңдаңыз:", reply_markup=services_keyboard_kz)
        elif text == "⬅️ Артқа":
            await message.answer("Негізгі мәзірге оралу.", reply_markup=main_keyboard_kz)
        elif text == "🎯 Кәсіби бағдар":
            kzt_price = int(42 * usd_kzt_rate) if usd_kzt_rate else 20160  # 42$ * 480₸
            await message.answer(
                "Кәсіби бағдар — адамның күшті жақтарын, қызығушылықтарын және құндылықтарын анықтауға көмектеседі, ол табысқа жетіп, шабыттанатын саланы табу үшін.\n\n"
                "- Қай салада маған ең жайлы және қызықты жұмыс істеуге болады?\n"
                "- Менің дағдыларымды қайда қолданып, өз орнымда сезіне аламын?\n"
                "- Шабыт пен дамуды сезіну үшін қай салада немесе ортада жұмыс іздеу керек?\n"
                "- Маған ең қолайлы кәсіби ортаны қалай таңдауға болады?\n\n"
                f"Ұзақтығы: 45 минут\n\n"
                f"Құны: {kzt_price}₸\n\n{rate_text}"
            )
        elif text == "🧠 Тұлға талдауы":
            await message.answer(
                "Өзіңізді, өз құндылығыңызды және сіздің құндылығыңыз қандай негізде құрылғанын түсінгенде, сіз өз әлсіздігіңізді көресіз.\n\n"
                "Өз табиғатыңызды түсіну — бұл тек мансап пен кәсіби мақсаттар туралы ғана емес, сонымен қатар ақша туралы.\n\n"
                f"Ұзақтығы: 90 минут\n\n"
                f"Құны: 8700₸/105$"
            )
        elif text == "🌟 Өзін-өзі жүзеге асыру саласы":
            await message.answer(
                "Өзін-өзі жүзеге асыру — бұл жеке тұлғаның әлеуетін жүзеге асыру, өз адамдық тағдырын, шақыруын орындау.\n\n"
                "Сізге сұрақ қоюға рұқсат етіңіз?\n\n"
                "Сіз өз кәсіби бағдарыңызбен, яғни өз іс-әрекет саласыңызбен сәйкес келесіз бе, сіз өз орныңызда боласыз ба?\n\n"
                "Біз сізге схема қалай жұмыс істейтінін көрсетеміз.\n\n"
                "Сіз өз жүзеге асыру салаңызда болсаңыз = ақша\n\n"
                f"Ұзақтығы: 45 минуттан 3 сессия\n\n"
                f"1-сессия - тұлға түрін талдау\n"
                f"2-сессия - дағдыларды анықтау (soft skills, hard skills, meta skills)\n"
                f"3-сессия - сіздің сұранысыңызға сәйкес мансаптық немесе бизнес-жоспардың қадамдық нұсқаулығы\n\n"
                f"Құны: 15000₸/186$"
            )
        elif text == "🧩 Бизнес/компания/ұйым/мансап талдауы":
            kzt_price = int(4200 * usd_kzt_rate) if usd_kzt_rate else 2016000  # 4200$ * 480₸
            await message.answer(
                "Бизнес талдауы — үлкен сандықта қазына іздеу сияқты: басты қазынаның қайда жатқанын дұрыс анықтау керек!\n\n"
                "Бұл барлық құрамдас бөліктерді, әсіресе сіздің және командаңыздың (қызметкерлердің) ішкі ресурстарын терең талдау және түсіну процесі.\n\n"
                "Бұл сырттан қарау, біраз жарық түсіру.\n"
                "Нәтижесінде, сіздің бизнесіңіз тек түсінікті болып қана қоймай, мақсаттарға жету үшін шынайы қуатты машинаға айналады!\n\n"
                f"Ұзақтығы: 3 - 6 ай\n\n"
                f"Құны: {kzt_price}₸\n\n{rate_text}"
            )
        elif text == "🎁 Тегін кеңес":
            await message.answer(
                "Біздің кеңесіміз сізге біздің кәсібилігімізді түсінуге және сенімді сезінуге көмектеседі.\n\n"
                "Сізге өте маңызды үш сұрақты дайындаңыз.\n\n"
                "Мүмкін бұл:\n"
                "- қарым-қатынас\n"
                "- некені тіркеу үшін ең жақсы күн\n"
                "- ақша коды\n"
                "- қай жерде шабыттыңыз жоғары\n"
                "- жыныстық серіктес\n"
                "және т.б.\n\n"
                "Сонда кеңес толығырақ әрі пайдалы болады.\n\n"
                "Ұзақтығы: 15 минут"
            )
        elif text == "☎️ Менеджермен байланыс":
            await message.answer(
                "Contact Manager\n\n"
                "Telegram: @ODEOlab\n\n"
                "📞 +79263454503"
            )
        elif text == "❓ Біз туралы":
            await message.answer("Learn more about us:", reply_markup=about_us_keyboard_kz)
        elif text == "💰 Төлем":
            await message.answer(
                "Payment is accepted in ways convenient for you.\n\n"
                "Contact the manager for details.\n\n"
                "@ODEOlab"
            )
        elif text == "💻 Цифрлық кеңесшілер":
            await message.answer(
                "Oksana Nikitina\n\n"
                "Founder of the international consulting association ODEO lab\n\n"
                "Practicing digital consultant for personal growth and business at SYUCAI TRAINING INSTITUTE, Dubai 🇦🇪 for over 6 years\n\n"
                "Curator of digital consultants in the Ural Federal District\n\n"
                "Head of the club in Tyumen"
            )
        elif text == "👥 Сарапшылар":
            await message.answer(
                "<b>Elena Turlak</b>\n\n"
                "Analyst and manager in logistics and trade\n\n"
                "Over 20 years of experience in network and traditional business\n\n"
                "<b>Dinara Safina</b>\n\n"
                "International-level lawyer\n\n"
                "Over 19 years of experience in legal consulting and auditing across jurisdictions in Russia, EU, UAE (company registrations, business support)\n\n"
                "Private legal practice for over 5 years (over 1000 successful court cases)"
            )
        elif text == "📑 Құжаттық базасы":
            await message.answer(
                "Official documents, licenses, certificates\n\n"
                "https://t.me/ODEOlab1"
            )
        elif text in ["📑 Құжаттық базасы", "💻 Цифрлық кеңесшілер", "👥 Сарапшылар", "⬅️ Артқа"]:
            if text == "⬅️ Артқа":
                await message.answer("Негізгі мәзірге оралу.", reply_markup=main_keyboard_kz)
            else:
                await message.answer("Ақпарат әзірлеу үстінде.")
        else:
            await message.answer("Мәзірден тармақты таңдаңыз.")

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))