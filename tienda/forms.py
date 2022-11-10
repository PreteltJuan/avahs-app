from django import forms
from .models import Contacto
from .models import Review

class formularioContacto(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = ["nombre","correo","consulta","mensaje",]
        
        
class calificacion(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['name','p0','p1','p2','review',]
        
        
        