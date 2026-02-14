def test_status_200(api_client):
    r = api_client.get(f"{api_client.base_url}/status/200", timeout=10)
    assert r.status_code == 200


def test_json_response(api_client):
    r = api_client.get(f"{api_client.base_url}/json", timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert "slideshow" in data
