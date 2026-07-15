from .conftest import client


def test_join_waitlist():

    response = client.post(
        "/api/v1/waitlist",
        json={
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "08012345678",
            "location": "Owerri"
        }
    )

    assert response.status_code == 201