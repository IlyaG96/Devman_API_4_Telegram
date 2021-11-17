from os import listdir
import telegram
import time


def send_picture_tg(photo_path: str,
                    chat_id: str,
                    bot: telegram.Bot,
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
        for picture in listdir(photo_path):
            bot.send_photo(chat_id=chat_id, photo=open(f"{photo_path}{picture}", 'rb'))
            time.sleep(delay)
