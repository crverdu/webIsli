from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),



    #encuestas
    path('encuesta', views.AgregarEncuesta.as_view(),name="add_encuesta"),
    path('encuesta/listar', views.ListarEncuesta.as_view(),name="list_encuesta"),
]
