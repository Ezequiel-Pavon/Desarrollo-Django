from django.urls import path
from . import views

"""
urls propias de la aplicación
"""


urlpatterns = {
    #el usuario entrara a esta redireción por urls
    path('', views.inicio, name='inicio'),
    #muesta el index
    path('turnos', views.turnos, name='turnos')
}
