from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sales'

    def ready(self) -> None:
        import apps.sales.signals
        return super().ready()
