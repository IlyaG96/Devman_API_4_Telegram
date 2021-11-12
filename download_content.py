import os
import pathlib
import requests
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import urlparse


def download_image(url: str,
                   PHOTO_PATH: str,
                   filename: str) -> None:
    """

    :param url:
    :param PHOTO_PATH:
    :param filename:
    :return:
    """
    pathlib.Path(PHOTO_PATH).mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f"{PHOTO_PATH}/{filename}", mode="wb") as file:
        file.write(response.content)


def get_nasa_apod(NASA_TOKEN: str) -> list:
    """

    :param NASA_TOKEN:
    :return:
    """
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}"
    payload = {
        "count": "50",
        "thumbs": "True"
               }
    response = requests.get(url, params=payload)
    urls = [picture["url"] for picture in response.json()]
    return urls


def get_nasa_epic(NASA_TOKEN: str) -> list:
    """

    :param NASA_TOKEN:
    :return:
    """
    urls =[]
    address = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_TOKEN}"
    response = requests.get(address)

    for picture in response.json():
        name = picture['image']
        date = datetime.fromisoformat(picture['date']).date().strftime('%Y/%m/%d')
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key={NASA_TOKEN}"
        urls.append(url)
    return urls


def show_extension(url:str) -> str:
    """

    :param url:
    :return:
    """
    url_path = urlparse(url).path
    path = os.path.split(url_path)[1]
    extension = os.path.splitext(path)[1]
    return extension


def download_pictures(urls: list):
    """

    :param urls:
    :return:
    """
    for number, url in enumerate(urls):
        extension = show_extension(url)
        filename = f"nasa{number}{extension}"
        try:
            download_image(url, PHOTO_PATH, filename)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    load_dotenv()
    NASA_TOKEN = os.getenv("NASA_TOKEN")
    PHOTO_PATH = os.getenv("PHOTO_PATH")
    urls = get_nasa_apod(NASA_TOKEN)
    download_pictures(urls)
# if not photos: download new photos
# Возможно, стоит удалять отправленные фото?
# Добавить возможность отправки описаний фотографий









