from django.apps import AppConfig

# file where we add our app to our project settings.py file to reference this class in installed apps
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    # import signals in app
    def ready(self):
        import users.signals
