import requests


def test_status_200():
    r = requests.get("https://httpbin.org/status/200", timeout=10)
    assert r.status_code == 200


def test_json_response():
    r = requests.get("https://httpbin.org/json", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "slideshow" in data
    assert "slides" in data["slideshow"]
