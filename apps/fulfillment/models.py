from django.conf import settings
from django.db import models

from apps.requests.models import GiftRequest


class Fulfillment(models.Model):
    class Status(models.TextChoices):
        MOCK_PAID = "mock_paid", "Mock paid"
        ORDERED = "ordered", "Ordered"
        SHIPPED = "shipped", "Shipped"
        LOCKER_READY = "locker_ready", "Locker ready"
        DELIVERED = "delivered", "Delivered"
        CANCELLED = "cancelled", "Cancelled"

    gift_request = models.OneToOneField(GiftRequest, on_delete=models.PROTECT)
    giver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    item_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    platform_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=32, choices=Status.choices, default=Status.MOCK_PAID)
    tracking_reference = models.CharField(max_length=128, blank=True)
    delivered_at = models.DateTimeField(null=True, blank=True)
