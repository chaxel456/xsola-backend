from .conftest import client


def test_subscriptions():

    response = client.get("/api/v1/subscriptions")

    assert response.status_code in [200, 401]