# Generated by Django 3.2.7 on 2021-09-13 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cleanings', '0002_cleaning_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleaning',
            name='cleaningtime',
        ),
    ]
