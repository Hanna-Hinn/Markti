from django.apps import AppConfig

"""
    BaseConfig:
        This will configure the application named base.
"""

class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
