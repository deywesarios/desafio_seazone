from django.contrib import admin

from clientes.actions import print_actions
from clientes.models import Cliente


@admin.register(Cliente)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ["nome", "cpf", "dtNascimento", "genero", "celular"]
    list_filter = ["genero"]
    search_fields = ["nome"]
    ordering = ["nome"]
    actions = [print_actions]

# admin.site.register(Cliente)

# @admin.register(Categoria)
# class CategoriaAdmin(admin.ModelAdmin):
#    pass
