from django import forms
from .models import persona,ciudad 
class PersonaForm(forms.ModelForm):
    class Meta:
        model= persona
        fields='__all__'

class CiudadForm(forms.ModelForm):
    class Meta:
        model=ciudad
        fields='__all__'    
