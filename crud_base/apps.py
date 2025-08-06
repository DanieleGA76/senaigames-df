from django.apps import AppConfig


class CrudBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud_base'
