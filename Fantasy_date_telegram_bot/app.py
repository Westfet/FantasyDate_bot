from aiogram.utils import executor
from config import dp
from handlers import question_handlers


async def on_startup(_):
    print('Бот вышел в онлайн')

#client.register_handlers_client(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)