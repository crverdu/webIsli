from .models import Dispositivo,Encuesta
from django import forms

class AddDispositivo(forms.ModelForm):
    description = forms.CharField(
    label='Descripcion', widget=forms.TextInput(attrs={'class': 'description'}), max_length=50, required=True, help_text='Nombre dispositivo')

    class Meta: 
        model= Dispositivo
        fields = ('description',)

class AddEncuesta(forms.ModelForm):
    apellido=forms.CharField(
        label='Apellido', widget=forms.TextInput(attrs={'class': 'apellido'}), max_length=80, required=True, help_text='Apellido (80 caract max)')
    nombre=forms.CharField(
        label='Nombre', widget=forms.TextInput(attrs={'class': 'nombre'}), max_length=80, required=True, help_text='Nombre (80 caract max)')    
    burbuja=forms.CharField(
        label='Burbuja', widget=forms.TextInput(attrs={'class': 'burbuja'}), max_length=1, required=True, help_text='Buebuja (A o B)')    
    email=forms.EmailField(
        label='Email', widget=forms.TextInput(attrs={'class': 'email'}), max_length=254, required=True, help_text='Se requiere una direccion de email valida.')
    bio=forms.CharField(
        label='Biografia', widget=forms.TextInput(attrs={'class': 'bio'}), max_length=200, required=True, help_text='Biografia breve 200 caract Max')    
    herramientas=forms.CharField(
        label='Herramientas', widget=forms.TextInput(attrs={'class': 'herramientas'}), max_length=200, required=True, help_text='Herramientas que conoces, word, excel, paint... 200 caract Max')    
    
    class Meta:
        model=Encuesta
        fields=['apellido','nombre','curso','burbuja','email','dispositivo','bio','herramientas']