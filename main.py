from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import Message

# Ваш токен бота (замените на ваш реальный токен!)
API_TOKEN = ''

# Создаем экземпляры бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

# Обработчик для всех остальных сообщений
@dp.message_handler()
async def all_messages(message: Message):
    await message.answer("Введите команду /start, чтобы начать общение.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
