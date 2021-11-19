import os
import sys
import dotenv
import telegram
import download_content
import astrolivebot
from argparse import ArgumentParser


def main() -> None:
    """
    Defines the behavior of the script depending on the command line argument,
    loads .env variables
    :return: None
    """

    parser = ArgumentParser(description="Chose mode")
    parser.add_argument("mode", help="Enter mode (bot or data)")
    mode = parser.parse_args().mode

    dotenv.load_dotenv()
    nasa_token = os.getenv("NASA_TOKEN")
    tg_token = os.getenv("TELEGRAM_TOKEN")
    photo_path = os.getenv("PHOTO_PATH")
    chat_id = os.getenv("CHAT_ID")
    delay_custom = int(os.getenv("DELAY_CUSTOM", default=86400))
    bot = telegram.Bot(token=tg_token)

    if mode not in ("bot", "data"):
        sys.exit("Wrong mode. Please use 'bot' or 'data'")

    elif mode == "bot":
        astrolivebot.send_picture_tg(photo_path,
                                     chat_id,
                                     bot,
                                     delay=delay_custom)
    else:
        urls = download_content.create_nasa_apod_base(nasa_token)
        download_content.download_nasa_images(urls,
                                              photo_path,
                                              nasa_token)


if __name__ == "__main__":
    main()
