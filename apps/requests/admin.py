from django.contrib import admin
from django.utils import timezone

from .models import GiftRequest


@admin.action(description="Publish selected requests")
def publish_requests(modeladmin, request, queryset):
    queryset.filter(status=GiftRequest.Status.PENDING_REVIEW).update(
        status=GiftRequest.Status.PUBLISHED,
        published_at=timezone.now(),
        rejection_reason="",
    )


@admin.action(description="Cancel selected requests")
def cancel_requests(modeladmin, request, queryset):
    queryset.filter(status__in=[GiftRequest.Status.DRAFT, GiftRequest.Status.PENDING_REVIEW, GiftRequest.Status.PUBLISHED]).update(
        status=GiftRequest.Status.CANCELLED,
    )


@admin.action(description="Reject selected requests")
def reject_requests(modeladmin, request, queryset):
    queryset.filter(status=GiftRequest.Status.PENDING_REVIEW).update(
        status=GiftRequest.Status.REJECTED,
    )


@admin.register(GiftRequest)
class GiftRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "requester", "category", "max_amount", "currency", "status", "published_at", "created_at")
    list_filter = ("status", "currency", "category")
    search_fields = ("title", "description", "requester__username", "requester__email")
    readonly_fields = ("created_at", "published_at")
    actions = (publish_requests, reject_requests, cancel_requests)
