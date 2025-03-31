import logging
from aiogram import Bot, Dispatcher, executor, types

# Настройки
API_TOKEN = '7914747184:AAGrMX61goPxd-K8UkE7uYapQ7Pg7-dDHX8'  # Замените на ваш токен
WEB_APP_URL = 'https://example.com'  # Замените на URL вашего веб-приложения

# Инициализация бота и диспетчера
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команд /start и /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # Создаем inline клавиатуру с кнопкой
    keyboard = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(
        text="Открыть веб-приложение 🌐",
        url=WEB_APP_URL
    )
    keyboard.add(web_app_button)

    # Текст сообщения
    welcome_text = (
        "Привет! Я демо-бот.\n"
        "Мои команды:\n"
        "/start - начать работу\n"
        "/help - помощь\n"
        "Жми кнопку ниже, чтобы открыть веб-приложение!"
    )

    await message.answer(welcome_text, reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)