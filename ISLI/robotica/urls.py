from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('encuesta', views.AgregarEncuesta.as_view(),name="add_encuesta"),
]
