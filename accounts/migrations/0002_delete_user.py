# Generated by Django 4.1.13 on 2023-11-27 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userrequests', '0002_alter_request_user_id'),
        ('index', '0004_item_category_alter_item_seller_id'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
