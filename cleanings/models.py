from django.db import models
from django.utils import timezone


class Cleaning(models.Model):
    APT_CHOICES = (
        ("APT 01", "APT 01"),
        ("APT 02", "APT 01"),
        ("APT 03", "APT 03"),
    )
    STATUS = (
        ("Cleaning", "Cleaning"),
    )
    employee = models.CharField(max_length=60, verbose_name="Employee Name")
    status = models.CharField(max_length=10, choices=STATUS)
    apt = models.CharField(max_length=10, choices=APT_CHOICES, verbose_name="Apartment")
    date = models.DateTimeField(default=timezone.now, verbose_name="Data")

    def __str__(self):
        return self.status
