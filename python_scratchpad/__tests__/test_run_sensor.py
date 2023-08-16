from unittest.mock import patch
from ..run_sensor import send_state
import requests


@patch("requests.post")
def test_send_state_success(post_mock):
    response = send_state({"id": 1})
    assert response is True
    post_mock.assert_called_once_with("https://en6msadu8lecg.x.pipedream.net/", json={"id": 1})


@patch("requests.post")
def test_send_state_fail(post_mock):
    post_mock.side_effect = requests.RequestException()
    response = send_state({"id": 1})
    assert response is False
    post_mock.assert_called_once_with("https://en6msadu8lecg.x.pipedream.net/", json={"id": 1})
