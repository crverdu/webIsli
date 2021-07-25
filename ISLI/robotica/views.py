from .forms import AddEncuesta
from .models import Encuesta
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

def index(request):
    return render(request, "index.html")

class AgregarEncuesta(SuccessMessageMixin,CreateView):
    model=Encuesta
    form_class=AddEncuesta
    template_name='encuesta.html'
    success_message = "Encuesta Enviada Correctamente"
    success_url=reverse_lazy('index')
    
    