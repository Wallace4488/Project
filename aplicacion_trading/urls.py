from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_senales, name='lista_senales'),
    path('api/senales/', views.api_lista_senales, name='api_lista_senales'),
]