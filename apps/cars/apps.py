from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.cars'

    def ready(self) -> None:
        import apps.cars.signals

        return super().ready()
