from .conftest import client


def test_get_devices():

    response = client.get("/api/v1/devices")

    assert response.status_code in [200, 401]