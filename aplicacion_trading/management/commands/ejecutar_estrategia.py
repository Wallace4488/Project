# from django.core.management.base import BaseCommand
# from aplicacion_trading.models import Signal
# from aplicacion_trading.estrategias.media_movil import EstrategiaMediaMovil
# from aplicacion_trading.conector_broker import ConectorBroker
# from datetime import datetime
# import calendar
# import logging

# logger = logging.getLogger(__name__)

# class Command(BaseCommand):
#     help = 'Ejecuta la estrategia de medias móviles y almacena las señales'

#     def handle(self, *args, **options):
#         hoy = datetime.today()
#         ultimo_dia = calendar.monthrange(hoy.year, hoy.month)[1]

#         # if hoy.day != ultimo_dia:
#         #     self.stdout.write("Hoy no es el último día del mes. Saliendo.")
#         #     return

#         tickers = [
#             "HAIL", "HOMZ", "IAI", "IAK", "IAT", "IBB", "ICF", "IDGT", "IDU", "IEDI",
#             "IEO", "IETC", "IEZ", "IFRA", "IHE", "IHF", "IHI", "ITA", "ITB", "IYC",
#             "IYE", "IYF", "IYG", "IYH", "IYJ", "IYK", "IYM", "IYR", "IYT", "IYW",
#             "IYZ", "KBE", "KBWB", "KBWP", "KBWR", "KBWY", "KCE", "KIE", "KRE", "LABD",
#             "LABU", "LTL", "MILN", "MLPA", "MLPX", "MORT"
#         ]
#         fecha_inicio = "2020-01-01"
#         fecha_fin = datetime.now().strftime('%Y-%m-%d')

#         estrategia = EstrategiaMediaMovil(tickers, fecha_inicio, fecha_fin)
#         estrategia.descargar_datos()
#         estrategia.calcular_medias_moviles()
#         estrategia.generar_senales()
#         senales_actuales = estrategia.obtener_senales_actuales()

#         Signal.objects.filter(date=hoy.date()).delete()

#         broker = ConectorBroker()
#         broker.conectar()

#         for symbol in tickers:
#             senal_valor = senales_actuales.get(symbol)
#             if senal_valor in ['BUY', 'SELL']:

#                 senal = Signal(date=hoy.date(), symbol=symbol, signal=senal_valor)
#                 senal.save()
#                 self.stdout.write(f"Guardada señal para {symbol}: {senal_valor}")

                
#                 accion = 'BUY' if senal_valor == 'BUY' else 'SELL'
#                 cantidad = 100  
#                 broker.realizar_orden(symbol, accion, cantidad)
#             else:
#                 self.stdout.write(f"No hay señal para {symbol}")

#         broker.desconectar()

from django.core.management.base import BaseCommand
from aplicacion_trading.models import Signal
from aplicacion_trading.estrategias.media_movil import EstrategiaMediaMovil
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Ejecuta la estrategia de medias móviles y almacena las señales'

    def handle(self, *args, **options):
        hoy = datetime.today()

        tickers = [
            "HAIL", "HOMZ", "IAI", "IAK", "IAT", "IBB", "ICF", "IDGT", "IDU", "IEDI",
            "IEO", "IETC", "IEZ", "IFRA", "IHE", "IHF", "IHI", "ITA", "ITB", "IYC",
            "IYE", "IYF", "IYG", "IYH", "IYJ", "IYK", "IYM", "IYR", "IYT", "IYW",
            "IYZ", "KBE", "KBWB", "KBWP", "KBWR", "KBWY", "KCE", "KIE", "KRE", "LABD",
            "LABU", "LTL", "MILN", "MLPA", "MLPX", "MORT"
        ]
        fecha_inicio = "2020-01-01"
        fecha_fin = datetime.now().strftime('%Y-%m-%d')

        estrategia = EstrategiaMediaMovil(tickers, fecha_inicio, fecha_fin)
        estrategia.descargar_datos()
        estrategia.calcular_medias_moviles()
        estrategia.generar_senales()
        senales_actuales = estrategia.obtener_senales_actuales()

        Signal.objects.filter(date=hoy.date()).delete()

        from aplicacion_trading.conector_broker import ConectorBroker

        broker = ConectorBroker()
        broker.conectar()

        for symbol in tickers:
            senal_valor = senales_actuales.get(symbol)
            if senal_valor in ['BUY', 'SELL']:
                senal = Signal(date=hoy.date(), symbol=symbol, signal=senal_valor)
                senal.save()
                self.stdout.write(f"Guardada señal para {symbol}: {senal_valor}")

                accion = 'BUY' if senal_valor == 'BUY' else 'SELL'
                cantidad = 100
                broker.realizar_orden(symbol, accion, cantidad)
            else:
                self.stdout.write(f"No hay señal para {symbol}")

        broker.desconectar()