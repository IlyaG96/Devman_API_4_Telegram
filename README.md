## Скрипт для управления Telegram ботом astrolive (или любым другим ботом)


Программа предназначена для работы с ботом в телеграм и для загрузки фотографий космоса с использованием API NASA

Клонируйте этот репозиторий себе на компьютер, создайте новое виртуальное окружение в папке с репозиторием, активируйте его и установите все пакеты командой 
```bash
pip install -r requirements.txt
```

Теперь создайте файл переменной окружения .env в папке с программой и заполните его согласно списка ниже:

**Это важное условие корректной работы программы**
```text
NASA_TOKEN = "your_nasa_token"
TELEGRAM_TOKEN = "your_telegram_token"
SPACEX_FLIGHT = number of spacex flight
CHAT_ID = "your_chat_bot_id"
PHOTO_PATH = path/to/photos
DELAY_CUSTOM = publish interval

```
Примечание по SPACEX_FLIGHT. Не все запуски имеют фото, попробуйте 100 или 64. Или 99, например


- Получить токен Телеграм:
  https://way23.ru/регистрация-бота-в-telegram.html
- Получить токен NASA:
  https://api.nasa.gov
- PHOTO_PATH можно узнать, например, командой ```pwd```, находясь в директории с проектом 
- DELAY_CUSTOM - задержка отправки (или интервал отправки) картинок. По умолчанию 86400 секунд - 24 часа. Настраивайте на свое усмотрение
- CHAT_ID - ссылка на канал в телеграме. Например, @astrolivechannel

Для отправки картинок необходимо создать базу с картинками, для этого
запустите скрипт командой для загрузки фотографий НАСА:
```bash
pyhon3 main.py nasa_data
```
Или для загрузки фотографий SPACEX:
```bash
pyhon3 main.py spacex_data
```
В вашей директории с программой появится папка, например, *photos* с картинками космоса.
Убедитесь, что она есть

Для того, чтобы бот начал отправлять картинки, его нужно запустить
```bash
python3 main.py bot
```
Бот будет отправлять все картинки из папки *photos* с интервалом CUSTOM_DELAY





  


