from django.apps import AppConfig

class ActivizaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'activiza'
    verbose_name = "Activiza"

    def ready(self):
        # This method will be executed once Django is fully initialized
        from django.contrib import admin
        from rest_framework.authtoken.models import TokenProxy #or Token based on your Django version
        try:
            admin.site.unregister(TokenProxy)
        except admin.sites.NotRegistered:
            pass
