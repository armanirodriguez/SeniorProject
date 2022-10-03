from django.apps import AppConfig


class HeardditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hearddit'

    def ready(self):
        import hearddit.signals  # noqa