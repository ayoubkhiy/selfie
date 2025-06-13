from django.db import models

# Create your models here.

from django.utils import timezone

class Selfie(models.Model):
    image = models.ImageField(upload_to='selfies/')
    date_taken = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Selfie {self.id} pris le {self.date_taken.strftime('%d/%m/%Y %H:%M')}"