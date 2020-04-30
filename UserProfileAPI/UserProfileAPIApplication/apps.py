from django.apps import AppConfig


class UserprofileapiapplicationConfig(AppConfig):
    name = 'UserProfileAPIApplication'

    def ready(self):
        import UserProfileAPIApplication.signals
