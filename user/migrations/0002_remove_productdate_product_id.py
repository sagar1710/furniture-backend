# Generated by Django 3.1.2 on 2021-01-01 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdate',
            name='product_id',
        ),
    ]
