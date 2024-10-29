# from django.apps import AppConfig
# import sys

# class AplicacionTradingConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'aplicacion_trading'

#     def ready(self):
#         if 'runserver' in sys.argv:
#             from . import scheduler
#             scheduler.start()

from django.apps import AppConfig
import sys

class AplicacionTradingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'aplicacion_trading'

    def ready(self):
        from . import scheduler
        scheduler.start()