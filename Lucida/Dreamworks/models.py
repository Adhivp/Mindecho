from django.db import models

# Create your models here.
# models.py
from django.db import models

class GeneratedImage(models.Model):
    image = models.ImageField(upload_to='generated_images/')