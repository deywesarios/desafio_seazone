from django.contrib import admin

from clientes.models import Cliente, Check
from cleanings.models import Cleaning


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "surname"]
    ordering = ["id"]

@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "amtpersons", "amtdaily", "location", "publicado", "value"]
    search_fields = ["name", "status", "location"]
    ordering = ["id"]

@admin.register(Cleaning)
class Cleaning(admin.ModelAdmin):
    list_display = ["apt", "status", "employee", "date"]
