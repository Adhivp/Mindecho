from django.db import models

# Create your models here.
class Name(models.Model):
    username = models.CharField(max_length=50)
