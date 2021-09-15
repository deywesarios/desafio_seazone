# Generated by Django 3.2.7 on 2021-09-11 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20210911_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='alterado',
        ),
        migrations.AddField(
            model_name='check',
            name='amtdaily',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Amount Daily'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='check',
            name='value',
            field=models.IntegerField(default=1, max_length=9),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='check',
            name='amtpersons',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Amount Persons'),
        ),
        migrations.AlterField(
            model_name='check',
            name='location',
            field=models.CharField(choices=[('AV. Búzios 1800, Jurerê Internacional, Florianópolis - SC. CEP 89650-100', 'Cobertura família com churrasqueira e piscina'), ('R. Prof. Renato Barbosa 227, Jurerê, Florianópolis - SC. CEP 88053-640', 'Studio Perto da Praia'), ('Alameda César Nascimento 138, Jurerê Internacional, Florianópolis - SC. CEP 88053-500', 'Conforto e tranquilidade na quadra do mar')], max_length=200),
        ),
    ]