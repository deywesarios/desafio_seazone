from django.apps import AppConfig


class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientes'
    icon_name = 'account_box'

class CleaningsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cleanings'
    icon_name = 'cleaning_services'

