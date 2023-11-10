import os

from src.main import get_name, main

# from src.main import get_api_response


# def test_get_api_response():
#     with requests_mock.Mocker() as m:
#         url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/market/auto-complete"
#         mock_response = {"hello": "world"}
#         m.get(url, json=mock_response)

#         result = get_api_response()
#         assert result == mock_response


def test_name_returns_normal_length():
    name = get_name("Short", "Name")
    assert name == "Short Name"


def test_name_returns_short_length():
    name = get_name("VeryVeryVeryVeryVery", "LongName")
    assert name == "V. LongName"


def test_main_writes_to_filesystem():
    main()
    the_dir = os.listdir()
    assert "output.csv" in the_dir
