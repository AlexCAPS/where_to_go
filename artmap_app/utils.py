import requests


def download_image(url):
    response = requests.get(url)
    return response.content


if __name__ == '__main__':
    download_image('https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/35cbdddf2799337d8b571d141edec616.JPG')