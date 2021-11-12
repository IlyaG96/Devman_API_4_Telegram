import os
import pathlib
import requests
from datetime import datetime
from urllib.parse import urlparse


def download_image(url: str,
                   PHOTO_PATH: str,
                   filename: str) -> None:
    """
    downloads one picture

    :param url: link to picture
    :param PHOTO_PATH: path to the folder with pictures
    :param filename: name of file
    :return: None
    """

    pathlib.Path(PHOTO_PATH).mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f"{PHOTO_PATH}/{filename}", mode="wb") as file:
        file.write(response.content)


def get_nasa_apod(NASA_TOKEN: str) -> list:
    """
    Tries to get a list of links with pictures, if it doesn't work, tries again

    :param NASA_TOKEN: NASA API Token
    :return: list with links

    :example

    urls = [url1.jpg, url2.jpg, someurl.gif] etc.

    """

    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_TOKEN}"
    payload = {
        "count": "5",
        "thumbs": "True"
               }
    response = requests.get(url, params=payload)
    try:
        urls = [picture["url"] for picture in response.json()]
        return urls
    except KeyError:
        get_nasa_apod(NASA_TOKEN)


def get_nasa_epic(NASA_TOKEN: str) -> list:
    """
    Tries to get a list of links with EPIC Earth pictures.
    :param NASA_TOKEN: NASA API Token
    :return: list with links
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


def show_extension(url: str) -> str:
    """
    Specifies the file extension

    :param url: link to the file
    :return: str extension of the file

    :example

    url = "https://example.com/txt/hello%20world.txt?v=9#python"
    returns .txt
    """

    url_path = urlparse(url).path
    path = os.path.split(url_path)[1]
    extension = os.path.splitext(path)[1]
    return extension


def download_pictures(urls: list,
                      PHOTO_PATH: str):
    """

    :param urls: list with links
    :param PHOTO_PATH: path to the folder with pictures
    :return: None
    """
    try:
        for number, url in enumerate(urls):
            extension = show_extension(url)
            filename = f"nasa{number}{extension}"
            download_image(url, PHOTO_PATH, filename)
    except TypeError:
        pass















