import os
import pathlib
import requests
from datetime import datetime
from urllib.parse import urlparse


def get_links_spacex() -> list:
    """returns a list of links to photos from the flight

    :return: list with links
    """
    flight_number = 64
    response = requests.get(f"https://api.spacexdata.com/v3/launches/{flight_number}")
    response.raise_for_status()
    urls = (response.json()['links']['flickr_images'])
    return urls


def download_spacex_photos(photo_path: str):
    """downloads SPACEX images

    :param photo_path:path to the folder with pictures
    :return: None
    """

    pathlib.Path(photo_path).mkdir(parents=True, exist_ok=True)
    urls = get_links_spacex()

    for number, url in enumerate(urls):
        extension = define_extension(url)
        filename = f"spacex{number}{extension}"
        response = requests.get(url)
        save_image(photo_path, filename, response)


def get_nasa_response(url: str,
                      nasa_token: str):
    """
    Receives a response from NASA using an url from a list with urls

    :param url: link to picture
    :param nasa_token: NASA API Token

    :return: None
    """

    payload = {
        "api_key": nasa_token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response


def save_image(photo_path: str,
               filename: str,
               response):
    """downloads one image

    :param photo_path: path to the folder with pictures
    :param filename: name of file
    :param response: response from NASA's site
    """
    with open(f"{photo_path}/{filename}", mode="wb") as file:
        file.write(response.content)


def create_nasa_apod_base(nasa_token: str) -> list:
    """
    Tries to get a list of links with pictures, if it doesn't work, tries again

    :param nasa_token: NASA API Token
    :return: list with links

    :example

    urls = [url1.jpg, url2.jpg, someurl.gif] etc.

    """

    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "count": "50",
        "thumbs": "True",
        "api_key": nasa_token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()

    urls = [picture["url"] for picture in response.json()]
    return urls


def create_nasa_epic_base(nasa_token: str) -> list:
    """
    Tries to get a list of links with EPIC Earth pictures.
    :param nasa_token: NASA API Token
    :return: list with links
    """

    urls = []
    payload = {
        "api_key": nasa_token
    }
    address = "https://api.nasa.gov/EPIC/api/natural/images"

    response = requests.get(address, params=payload)
    response.raise_for_status()

    for picture in response.json():
        name = picture["image"]
        date = datetime.fromisoformat(picture["date"]).date().strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png"
        urls.append(url)
    return urls


def define_extension(url: str) -> str:
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


def download_nasa_images(urls: list,
                         photo_path: str,
                         nasa_token):
    """downloads NASA's images

    :param urls: list with links
    :param photo_path: path to the folder with pictures
    :param nasa_token: NASA API Token

    :return: None
    """

    pathlib.Path(photo_path).mkdir(parents=True, exist_ok=True)

    for number, url in enumerate(urls):
        extension = define_extension(url)
        filename = f"nasa{number}{extension}"
        response = get_nasa_response(url, nasa_token)
        if extension:
            save_image(photo_path, filename, response)


download_spacex_photos(photo_path="/Users/ilyagabdrakhmanov/PycharmProjects/Devman_API_4_Telegram/photos/")