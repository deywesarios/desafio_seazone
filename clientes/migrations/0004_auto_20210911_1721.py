# Generated by Django 3.2.7 on 2021-09-11 20:21

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_alter_cliente_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Cobertura família c/ churrasqueira piscina', 'AV. Búzios 1800, Jurerê Internacional, Florianópolis - SC. CEP 89650-100'), ('Studio Perto da Praia', 'R. Prof. Renato Barbosa 227, Jurerê, Florianópolis - SC. CEP 88053-640'), ('Conforto e tranquilidade na quadra do mar', 'Alameda César Nascimento 138, Jurerê Internacional, Florianópolis - SC. CEP 88053-500')], max_length=200)),
                ('amtpersons', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('checkin', models.DateTimeField(auto_now_add=True)),
                ('alterado', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('check-in', 'Check-In'), ('check-out', 'Check-Out')], default='check-in', max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='alterado',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='checkin',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='publicado',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='status',
        ),
    ]
