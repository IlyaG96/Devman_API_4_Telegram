import os
import sys
import dotenv
import telegram
import download_content
import astrolivebot_script
from argparse import ArgumentParser


def main() -> None:
    """
    Defines the behavior of the script depending on the command line argument
    :return: None
    """
    parser = ArgumentParser(description='Chose mode')
    parser.add_argument('mode', help="Enter mode (bot or data)")
    mode = parser.parse_args().mode

    dotenv.load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    tg_token = os.getenv("TELEGRAM_TOKEN")
    photo_path = os.getenv("PHOTO_PATH")
    chat_id = os.getenv("CHAT_ID")
    delay_custom = int(os.getenv("DELAY_CUSTOM", default=86400))
    bot = telegram.Bot(token=tg_token)

    if mode not in ("bot", "data"):
        sys.exit("Wrong mode. Please use 'bot' or 'data")

    elif mode == "bot":
        files_base = astrolivebot_script.generate_pictures_base(photo_path)
        astrolivebot_script.send_picture_tg(photo_path,
                                            chat_id,
                                            bot,
                                            files_base,
                                            delay=delay_custom)
    else:
        urls = download_content.get_nasa_apod(nasa_token)
        download_content.download_pictures(urls,
                                           photo_path)


if __name__ == '__main__':
    main()
