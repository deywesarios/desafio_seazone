from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    GENRE_CHOICES = (
        ("Masculine", "Masculine"),
        ("Feminine", "Feminine"),
        ("Do not inform", "Do not inform"),
    )
    name = models.CharField(max_length=60, verbose_name="Name")
    surname = models.CharField(max_length=60, verbose_name="Surname")
    genre = models.CharField(max_length=60, choices=GENRE_CHOICES)
    birthday = models.DateField(blank=True, null=True, verbose_name="Birthday")
    phone = models.CharField(max_length=16, blank=True, null=True, verbose_name="Phone")

    def __str__(self):
        return self.name


class Check(models.Model):
    LOCATION_CHOICES = (
        ("AV. Búzios 1800, Jurerê Internacional, Florianópolis - SC. CEP 89650-100",  # PLACE
         "Cobertura família com churrasqueira e piscina"),
        ("R. Prof. Renato Barbosa 227, Jurerê, Florianópolis - SC. CEP 88053-640",  # PLACE
         "Studio Perto da Praia"),
        ("Alameda César Nascimento 138, Jurerê Internacional, Florianópolis - SC. CEP 88053-500",  # PLACE
         "Conforto e tranquilidade na quadra do mar"),
    )
    STATUS = (
        ("check-in", "Check-In"),
        ("check-out", "Check-Out"),
    )
    name = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Name")
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    publicado = models.DateTimeField(default=timezone.now, verbose_name="Data")
    amtpersons = models.IntegerField(validators=[MinValueValidator(1),
                                                 MaxValueValidator(10)],
                                     verbose_name="Amount Persons")
    amtdaily = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(30)],
                                   verbose_name="Amount Daily")
    value = models.CharField(max_length=9, verbose_name="Value")
    checkin = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default="check-in")

    def __str__(self):
        return self.status
