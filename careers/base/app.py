from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    name = 'careers.base'

    def ready(self):
        # The app is now ready. Include any monkey patches here.
        pass
