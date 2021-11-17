import os
import pathlib
import requests
from datetime import datetime
from urllib.parse import urlparse


def download_image(url: str,
                   photo_path: str,
                   filename: str) -> None:
    """
    downloads one picture

    :param url: link to picture
    :param photo_path: path to the folder with pictures
    :param filename: name of file
    :return: None
    """

    pathlib.Path(photo_path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f"{photo_path}/{filename}", mode="wb") as file:
        file.write(response.content)


def get_nasa_apod(nasa_token: str) -> list:
    """
    Tries to get a list of links with pictures, if it doesn't work, tries again

    :param nasa_token: NASA API Token
    :return: list with links

    :example

    urls = [url1.jpg, url2.jpg, someurl.gif] etc.

    """

    url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_token}"
    payload = {
        "count": "5",
        "thumbs": "True"
               }
    response = requests.get(url, params=payload)
    try:
        urls = [picture["url"] for picture in response.json()]
        return urls
    except KeyError:
        get_nasa_apod(nasa_token)


def get_nasa_epic(nasa_token: str) -> list:
    """
    Tries to get a list of links with EPIC Earth pictures.
    :param nasa_token: NASA API Token
    :return: list with links
    """
    urls =[]
    address = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={nasa_token}"
    response = requests.get(address)

    for picture in response.json():
        name = picture['image']
        date = datetime.fromisoformat(picture['date']).date().strftime('%Y/%m/%d')
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key={nasa_token}"
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
                      photo_path: str):
    """

    :param urls: list with links
    :param photo_path: path to the folder with pictures
    :return: None
    """
    try:
        for number, url in enumerate(urls):
            extension = show_extension(url)
            filename = f"nasa{number}{extension}"
            download_image(url, photo_path, filename)
    except TypeError:
        pass


