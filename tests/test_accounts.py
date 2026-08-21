import pytest
from django.urls import reverse

from apps.accounts.models import User


@pytest.mark.django_db
def test_signup_creates_user(client):
    response = client.post(reverse("signup"), {
        "email": "new@example.com",
        "username": "newuser",
        "age_band": "25-29",
        "country": "GR",
        "password1": "Strong-password-123!",
        "password2": "Strong-password-123!",
    })
    assert response.status_code == 302
    assert User.objects.filter(email="new@example.com").exists()


@pytest.mark.django_db
def test_login_and_logout(client):
    User.objects.create_user(email="user@example.com", username="user", password="Strong-password-123!")
    response = client.post(reverse("login"), {"email": "user@example.com", "password": "Strong-password-123!"})
    assert response.status_code == 302
    response = client.post(reverse("logout"))
    assert response.status_code == 302
