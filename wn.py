import requests


def fetch_word_of_the_day(api_key: str) -> str:
    return requests.request("GET", f"https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key={api_key}").json()[
        "word"]
