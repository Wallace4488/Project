# from ib_insync import *
# import logging

# logger = logging.getLogger(__name__)

# class ConectorBroker:
#     def __init__(self, host='127.0.0.1', port=4002, client_id=1):
#         self.ib = IB()
#         self.host = host
#         self.port = port
#         self.client_id = client_id

#     def conectar(self):
#         try:
#             self.ib.connect(self.host, self.port, clientId=self.client_id)
#             logger.info("Conectado a Interactive Brokers.")
#         except Exception as e:
#             logger.error(f"Error al conectar con Interactive Brokers: {e}")

#     def realizar_orden(self, symbol, accion, cantidad):
#         try:
#             contrato = Stock(symbol, 'SMART', 'USD')
#             orden = MarketOrder(accion, cantidad)
#             trade = self.ib.placeOrder(contrato, orden)
#             logger.info(f"Orden {accion} realizada para {symbol}")
#             return trade
#         except Exception as e:
#             logger.error(f"Error al realizar la orden para {symbol}: {e}")

#     def desconectar(self):
#         self.ib.disconnect()
#         logger.info("Desconectado de Interactive Brokers.")

import logging
import asyncio

logger = logging.getLogger(__name__)

class ConectorBroker:
    def __init__(self, host='127.0.0.1', port=4002, client_id=1):
        self.ib = None
        self.host = host
        self.port = port
        self.client_id = client_id

    def conectar(self):
        try:
            asyncio.get_event_loop()
        except RuntimeError:
            asyncio.set_event_loop(asyncio.new_event_loop())
        from ib_insync import IB

        try:
            self.ib = IB()
            self.ib.connect(self.host, self.port, clientId=self.client_id)
            logger.info("Conectado a Interactive Brokers.")
        except Exception as e:
            logger.error(f"Error al conectar con Interactive Brokers: {e}")

    def realizar_orden(self, symbol, accion, cantidad):
        from ib_insync import Stock, MarketOrder

        try:
            contrato = Stock(symbol, 'SMART', 'USD')
            orden = MarketOrder(accion, cantidad)
            trade = self.ib.placeOrder(contrato, orden)
            logger.info(f"Orden {accion} realizada para {symbol}")
            return trade
        except Exception as e:
            logger.error(f"Error al realizar la orden para {symbol}: {e}")

    def desconectar(self):
        if self.ib:
            self.ib.disconnect()
            logger.info("Desconectado de Interactive Brokers.")