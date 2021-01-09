import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from bot_config import API_TOKEN
from requests_tools import http_get_request_to_txt
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def response_sender(message: types.Message):
    """Срабатывает только на текстовые сообщения и в случае успешного запроса присылает .txt файл с ответом"""
    text = message.text
    file_name = f"{message.from_user.id}_{str(message.message_id)}.txt"
    try:
        txt_file, file_path = http_get_request_to_txt(text, file_name)
    except requests.exceptions.InvalidURL:
        await bot.send_message(message.chat.id, "Некорректная ссылка.")
    else:
        await bot.send_document(message.chat.id, txt_file)
        txt_file.close()
        os.remove(file_path)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
