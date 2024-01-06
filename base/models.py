from django.db import models

# Create your models here.
class Message(models.Model):
    content = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    