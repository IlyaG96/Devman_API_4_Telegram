from os import listdir
import telegram
import time



def send_text_message_tg(bot: telegram.Bot,
                         CHAT_ID: str,
                         ) -> None:
    """
    future function to send photo's descriptions
    :param bot: telegram.Bot object
    :return: None
    """
    bot.send_message(chat_id=CHAT_ID, text="Your text message")


def generate_pictures_base(PHOTO_PATH: str) -> list:
    """
    generates list that containing photo's names
    :param PHOTO_PATH: .env variable - directory with your photos
    :return: list with photos names
    """
    pictures_base = listdir(PHOTO_PATH)
    return pictures_base


def send_picture_tg(PHOTO_PATH: str,
                    CHAT_ID: str,
                    bot: telegram.Bot,
                    files_base: list,
                    delay = 86400,
                    ):
    """

    :param PHOTO_PATH:
    :param bot:
    :param files_base:
    :return:
    """

    while True:
        for file in files_base:
            bot.send_photo(chat_id=CHAT_ID, photo=open(f"{PHOTO_PATH}{file}", 'rb'))
            time.sleep(delay)


