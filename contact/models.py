from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()