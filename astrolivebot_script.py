from dotenv import load_dotenv
from os import listdir
import os
import telegram


def send_text_message_tg(bot):
    bot.send_message(chat_id=CHAT_ID, text="here is my first message")


def generate_pictures_base(PHOTO_PATH: str) -> list:
    """
    generates list that containing photo's names
    :param PHOTO_PATH: .env variable - directory with your photos
    :return: list with photos names
    """
    pictures_base = listdir(PHOTO_PATH)
    return pictures_base


def send_picture_tg(PHOTO_PATH, bot, files_base, ):
    for file in files_base:
        bot.send_photo(chat_id=CHAT_ID, photo=open(f"{PHOTO_PATH}{file}", 'rb'))


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
    PHOTO_PATH = os.getenv("PHOTO_PATH")
    CHAT_ID = os.getenv("CHAT_ID")
    bot = telegram.Bot(token=TG_TOKEN)
    files_base = generate_pictures_base(PHOTO_PATH)
    send_picture_tg(PHOTO_PATH, bot, files_base)
