from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.utils import timezone

class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField()
    experience = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]