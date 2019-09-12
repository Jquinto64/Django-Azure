from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=255, null = False)
    description = models.TextField()