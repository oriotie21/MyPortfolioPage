from django.db import models

# Create your models here.
class Achievement(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
class ContactMessage(models.Model):
    user = models.CharField(max_length=20)
    content = models.TextField()
    #ip_addr = models.TextField()
    date = models.DateTimeField()
class LanguageImage(models.Model):
    content = models.TextField()
