from django.contrib import admin

from .models import GiftRequest


@admin.register(GiftRequest)
class GiftRequestAdmin(admin.ModelAdmin):
    list_display = ("title", "requester", "category", "max_amount", "currency", "status", "created_at")
    list_filter = ("status", "currency", "category")
    search_fields = ("title", "description", "requester__username", "requester__email")
