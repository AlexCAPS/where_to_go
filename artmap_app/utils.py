import requests


def download_image(url):
    response = requests.get(url)
    return response.content


def download_place_file(url):
    response = requests.get(url)
    return response.json()
