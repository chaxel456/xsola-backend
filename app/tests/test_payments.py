from .conftest import client


def test_get_payments():

    response = client.get("/api/v1/payments")

    assert response.status_code in [200, 401]