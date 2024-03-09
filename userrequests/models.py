from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    description = models.TextField()
