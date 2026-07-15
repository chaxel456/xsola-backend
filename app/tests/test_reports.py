from .conftest import client


def test_reports():

    response = client.get("/api/v1/reports")

    assert response.status_code in [200, 401]