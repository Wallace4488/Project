from django.shortcuts import render
from .models import Signal
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SignalSerializer

def lista_senales(request):
    hoy = datetime.today().date()
    senales = Signal.objects.filter(date=hoy)
    return render(request, 'aplicacion_trading/lista_senales.html', {'senales': senales})


@api_view(['GET'])
def api_lista_senales(request):
    hoy = datetime.today().date()
    senales = Signal.objects.filter(date=hoy)
    serializer = SignalSerializer(senales, many=True)
    return Response(serializer.data)