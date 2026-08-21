import pytest
from django.urls import reverse

from apps.accounts.models import User
from apps.requests.models import GiftRequest


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser(email="admin@example.com", username="admin", password="Strong-password-123!")


@pytest.mark.django_db
def test_published_request_is_public(client, user):
    gift_request = GiftRequest.objects.create(requester=user, title="Monitor", max_amount=200, status=GiftRequest.Status.PUBLISHED)
    response = client.get(reverse("home"))
    assert response.status_code == 200
    assert gift_request.title.encode() in response.content
