from django.contrib import admin


@admin.action(description='Imprimir')
def print_actions(modeladmin, request, queryset):
    pass