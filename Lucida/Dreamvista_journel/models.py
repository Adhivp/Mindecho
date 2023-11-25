from django.db import models

# Create your models here.

class journel(models.Model):
    date = models.DateField()
    title = models.CharField(max_length= 250,null=True)
    experience = models.TextField()
