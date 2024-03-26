import requests_mock

from ..main import get_api_response


def test_get_api_response():
    with requests_mock.Mocker() as m:
        url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
        mock_response = {"hello": "world"}
        m.get(url, json=mock_response)

        result = get_api_response()
        assert result == mock_response
