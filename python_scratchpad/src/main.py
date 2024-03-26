import os
from typing import Any

from dotenv import load_dotenv
from requests import get

# ruff: noqa:T201


def get_api_response() -> Any:  # noqa: ANN401
    _ = load_dotenv()

    url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
    querystring = {"query": "apple"}
    headers = {
        "X-RapidAPI-Key": os.environ["X-RAPIDAPI-KEY"],
        "X-RapidAPI-Host": os.environ["X-RAPDIDAPI-HOST"],
    }
    response = get(url, headers=headers, params=querystring, timeout=5)
    return response.json()


if __name__ == "__main__":
    print(get_api_response())
