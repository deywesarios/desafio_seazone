<<<<<<< HEAD
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
=======
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
>>>>>>> 7ecf0588ac716eb8e28267220c531014cd74540b
