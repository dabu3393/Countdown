from django.db import models

# Create your models here.
class Countdown(models.Model):
    target_date = models.DateTimeField()
    description = models.CharField(max_length=255)