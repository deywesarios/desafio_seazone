# Generated by Django 3.2.7 on 2021-09-07 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('surname', models.CharField(max_length=60, verbose_name='Surname')),
                ('genre', models.IntegerField(choices=[('Masculine', 'Masculine'), ('Feminine', 'Feminine'), ('Do not inform', 'Do not inform')])),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, verbose_name='Phone')),
                ('checkin', models.DateTimeField(auto_now_add=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('check-in', 'Check-In'), ('check-out', 'Check-Out')], default='check-in', max_length=10)),
            ],
        ),
    ]