<<<<<<< HEAD
# Generated by Django 3.2.7 on 2021-09-13 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cleanings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]
=======
# Generated by Django 3.2.7 on 2021-09-13 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cleanings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data'),
        ),
    ]
>>>>>>> 7ecf0588ac716eb8e28267220c531014cd74540b
