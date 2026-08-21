from django.db import models


class Profile(models.Model):
    age_band = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
