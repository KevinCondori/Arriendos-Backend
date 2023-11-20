from django.apps import AppConfig


class LeasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'leases'
    def ready(self):
        from leases import signals