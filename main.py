import requests
import pathlib
from urllib.parse import urlparse
from datetime import datetime
import os


def download_image(url: str,
                   path: str,
                   filename):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    response = requests.get(url)
    response.raise_for_status()

    with open(f"{path}/{filename}", mode="wb") as file:
        file.write(response.content)


def get_info_spacex():

    response = requests.get("https://api.spacexdata.com/v3/launches/64")
    image_links = (response.json()['links']['flickr_images'])

    return image_links


def fetch_spacex_launch(image_links):
    for url_number, url in enumerate(image_links):
        filename = f"{url_number}.jpg"
        download_image(url, path, filename)


def get_NASA_apod(NASA_token):
    url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_token}"
    payload = {
        "count": "50",
        "thumbs": "True"
               }
    response = requests.get(url, params=payload)
    urls = [picture["url"] for picture in response.json()]
    return urls


def get_nasa_epic(NASA_token):
    urls =[]
    address = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={NASA_token}"
    response = requests.get(address)

    for picture in response.json():
        name = picture['image']
        date = datetime.fromisoformat(picture['date']).date().strftime('%Y/%m/%d')
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key={NASA_token}"
        urls.append(url)
    return urls


def show_extension(url):
    url_path = urlparse(url).path
    path = os.path.split(url_path)[1]
    extension = os.path.splitext(path)[1]
    return extension


def download_pictures(urls):
    for number, url in enumerate(urls):
        extension = show_extension(url)
        filename = f"nasa{number}{extension}"
        download_image(url, path, filename)


if __name__ == '__main__':
    pass
#  path
#  token







