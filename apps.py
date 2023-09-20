from django.apps import AppConfig


class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Choose the appropriate auto field for database backend
    name = 'yourappname'
    verbose_name = 'Your App Name'
