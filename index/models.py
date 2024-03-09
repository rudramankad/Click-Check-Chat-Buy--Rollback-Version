# from django.db import models

# class Item(models.Model):
#     item_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     condition = models.CharField(max_length=255)
#     # photos = models.CharField(max_length=255)
#     photos = models.ImageField()
#     seller_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, default='Uncategorized')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=255)
    photos = models.ImageField(upload_to='items/photos')  # Specify the upload directory
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
