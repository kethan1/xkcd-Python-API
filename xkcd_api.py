import requests
import random

def get_latest_comic() -> dict:
    response = requests.get("https://xkcd.com/info.0.json")
    return response.json()

def download_image(json_content: dict) -> None:
    img = requests.get(json_content["img"])
    with open("comic.png", "wb") as comicbook:
        comicbook.write(img.content)

def get_comic(number: int) -> dict:
    random_comic = requests.get(f"https://xkcd.com/{number}/info.0.json")
    return random_comic.json()

def get_random_comic() -> dict:
    latest_comic_num = get_latest_comic()["num"]
    random_comic = requests.get(f"https://xkcd.com/{random.randint(1, latest_comic_num)}/info.0.json")
    return random_comic.json()
