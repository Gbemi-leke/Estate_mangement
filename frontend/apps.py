from django.apps import AppConfig


class FrontendConfig(AppConfig):
    name = 'frontend'

    def ready(self):
        from frontend import signals