from django import forms
from .models import Contacto
from .models import calificar

class formularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre","correo","consulta","mensaje","avisos"]
        
        
class calificacion(forms.ModelForm):

    class Meta:
        model = calificar
        fields = ['rating','name','review',]
        
        
        