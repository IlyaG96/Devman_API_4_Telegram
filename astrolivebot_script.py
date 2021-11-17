from os import listdir
import telegram
import time


def generate_pictures_base(photo_path: str) -> list:
    """
    generates list that containing photo's names
    :param photo_path: .env variable - directory with your photos
    :return: list with photos names
    """
    pictures_base = listdir(photo_path)
    return pictures_base


def send_picture_tg(photo_path: str,
                    chat_id: str,
                    bot: telegram.Bot,
                    pictures_base: list,
                    delay = 86400,
                    ):
    """
    Sends pictures to telegrams with a selected delay
    :param photo_path: .env variable - directory with your photos
    :param bot: telegram.Bot object
    :param pictures_base: list with pictures names
    :return: None
    """

    while True:
        for picture in pictures_base:
            bot.send_photo(chat_id=chat_id, photo=open(f"{photo_path}{picture}", 'rb'))
            time.sleep(delay)
