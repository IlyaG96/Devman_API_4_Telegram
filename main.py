import sys
import astrolivebot_script
import download_content
import os
import dotenv
import telegram
from argparse import ArgumentParser


def main() -> None:
    """

    :return: None
    """
    parser = ArgumentParser(description='Chose mode')
    parser.add_argument('mode', help="Enter mode (bot or data)")
    mode = parser.parse_args().mode
    if mode not in ("bot", "data"):
        sys.exit("Wrong mode. Please use 'bot' or 'data")
    elif mode == "bot":
        files_base = astrolivebot_script.generate_pictures_base(PHOTO_PATH)
        astrolivebot_script.send_picture_tg(PHOTO_PATH, CHAT_ID, bot, files_base, delay=DELAY_CUSTOM)
    else:
        urls = download_content.get_nasa_apod(NASA_TOKEN)
        download_content.download_pictures(urls, PHOTO_PATH)


if __name__ == '__main__':
    dotenv.load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
    PHOTO_PATH = os.getenv("PHOTO_PATH")
    CHAT_ID = os.getenv("CHAT_ID")
    DELAY_CUSTOM = int(os.getenv("DELAY_CUSTOM"))
    bot = telegram.Bot(token=TG_TOKEN)
    main()







