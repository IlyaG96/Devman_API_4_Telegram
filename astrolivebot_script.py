from dotenv import load_dotenv
import os
import telegram


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv("TELEGRAM_TOKEN")
    chat_id = "@astrolivechannel"
    bot = telegram.Bot(token=TG_TOKEN)
    bot.send_message(chat_id=chat_id, text="here is my first message")
    print(bot.get_me())