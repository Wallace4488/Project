from django.db import models

class Signal(models.Model):
    date = models.DateField()
    symbol = models.CharField(max_length=10)
    signal = models.CharField(max_length=4) 

    def __str__(self):
        return f"{self.date} - {self.symbol}: {self.signal}"