from django import forms
from django.forms import extras
from django.forms import ModelForm
from vecinos.apps.registro.models import Vecino, Casa, Calle
from datetime import date


class AgregaVecinoForm(forms.Form):
    calle = forms.ModelChoiceField(queryset=Calle.objects.all())
    numero = forms.IntegerField()
    telefono = forms.IntegerField()
    nombre = forms.CharField()

class CasaForm(forms.ModelForm):
	class Meta:
		model = Casa
		fields = ['calle', 'numero']