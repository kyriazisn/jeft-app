from django.db import models


class CatalogItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
