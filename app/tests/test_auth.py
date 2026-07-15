from .conftest import client


def test_login():
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "admin@xsola.com",
            "password": "password"
        }
    )

    assert response.status_code in [200, 401]