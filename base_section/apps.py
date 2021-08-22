from django.apps import AppConfig


class BaseSectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_section'
