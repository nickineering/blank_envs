import os

from dotenv import load_dotenv
from requests import get


def get_api_response():
    load_dotenv()

    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
    querystring = {"query": "apple"}
    headers = {
        "X-RapidAPI-Key": os.environ["X-RAPIDAPI-KEY"],
        "X-RapidAPI-Host": os.environ["X-RAPDIDAPI-HOST"],
    }
    response = get(url, headers=headers, params=querystring)
    return response.json()


if __name__ == "__main__":
    print(get_api_response())
