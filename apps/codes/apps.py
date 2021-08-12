from django.apps import AppConfig


class CodesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.codes'

    def ready(self) -> None:
        import apps.codes.signals
        return super().ready()
