from django.db import models

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True)
    password = models.CharField(max_length=50)