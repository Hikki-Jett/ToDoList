from django.db import models
from django.utils import timezone


# Create your models here.
class Task_list(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length= 500, default="")
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
