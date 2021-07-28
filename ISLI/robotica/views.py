from .forms import AddEncuesta
from .models import Encuesta
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

def index(request):
    return render(request, "index.html")

#Agregar Encuestas
class AgregarEncuesta(SuccessMessageMixin,CreateView):
    model=Encuesta
    form_class=AddEncuesta
    template_name='encuestas/encuesta.html'
    success_message = "Encuesta Enviada Correctamente"
    success_url=reverse_lazy('index')
    

#Listar Encuestas admin preview
class ListarEncuesta(PermissionRequiredMixin,ListView):
    permission_required = ('robotica.change_curso')
    model = Encuesta
    template_name='encuestas/resultados.html'
    queryset = Encuesta.objects.all().order_by("-id")