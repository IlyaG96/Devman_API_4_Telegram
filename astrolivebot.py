from os import listdir
import telegram
import time


def send_picture_tg(photo_path: str,
                    chat_id: str,
                    bot: telegram.Bot,
                    delay=86400,
                    ):
    """
    Sends pictures to telegrams with a selected delay
    :param photo_path: .env variable - directory with your photos
    :param chat_id: .env variable - @name of your channel
    :param bot: telegram.Bot object
    :param delay: time between two posts
    :return: None
    """

    while True:
        for picture in listdir(photo_path):
            with open(f"{photo_path}{picture}", "rb") as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            time.sleep(delay)
