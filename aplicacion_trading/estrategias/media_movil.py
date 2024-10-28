import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime

class EstrategiaMediaMovil:
    def __init__(self, tickers, fecha_inicio, fecha_fin):
        self.tickers = tickers
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.data = None
        self.sma_50 = {}
        self.sma_100 = {}
        self.signals = {}

    def descargar_datos(self):
        self.data = yf.download(self.tickers, start=self.fecha_inicio, end=self.fecha_fin)

    def calcular_medias_moviles(self):
        for ticker in self.tickers:
            adj_close = self.data['Adj Close'][ticker]
            self.sma_50[ticker] = adj_close.rolling(window=50).mean()
            self.sma_100[ticker] = adj_close.rolling(window=100).mean()

    def generar_senales(self):
        for ticker in self.tickers:
            sma_short = self.sma_50[ticker]
            sma_long = self.sma_100[ticker]
            signal = np.where(sma_short > sma_long, 'BUY',
                              np.where(sma_short < sma_long, 'SELL', 'HOLD'))
            self.signals[ticker] = signal[-1]  # Última señal

    def obtener_senales_actuales(self):
        return self.signals