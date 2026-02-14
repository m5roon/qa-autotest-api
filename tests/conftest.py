import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://httpbin.org"


@pytest.fixture()
def api_client(base_url):
    session = requests.Session()
    session.base_url = base_url
    yield session
    session.close()
