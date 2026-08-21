from decimal import Decimal

import pytest
from django.urls import reverse

from apps.accounts.models import User
from apps.requests.models import GiftRequest


@pytest.fixture
def user(db):
    return User.objects.create_user(email="requester@example.com", username="requester", password="Strong-password-123!")


@pytest.mark.django_db
def test_anonymous_user_is_redirected(client):
    response = client.get(reverse("create_request"))
    assert response.status_code == 302
    assert reverse("login") in response.url


@pytest.mark.django_db
def test_authenticated_user_can_create_request(client, user):
    client.force_login(user)
    response = client.post(reverse("create_request"), {"title": "Gaming monitor", "description": "27 inch monitor", "category": "Technology", "requested_url": "", "max_amount": "200"})
    assert response.status_code == 302
    gift_request = GiftRequest.objects.get(requester=user)
    assert gift_request.status == GiftRequest.Status.PENDING_REVIEW
    assert gift_request.currency == "EUR"
    assert gift_request.max_amount == Decimal("200")


@pytest.mark.django_db
def test_request_cannot_exceed_500(client, user):
    client.force_login(user)
    response = client.post(reverse("create_request"), {"title": "Expensive item", "description": "Item", "category": "Other", "requested_url": "", "max_amount": "500.01"})
    assert response.status_code == 200
    assert not GiftRequest.objects.exists()


@pytest.mark.django_db
def test_user_can_have_only_one_active_request(client, user):
    GiftRequest.objects.create(requester=user, title="Existing", max_amount=100, currency="EUR", status=GiftRequest.Status.PENDING_REVIEW)
    client.force_login(user)
    response = client.get(reverse("create_request"))
    assert response.status_code == 200
    assert "already have an active request" in response.content.decode().lower()
