from django.shortcuts import render
from vecinos.apps.registro.forms import AgregaVecinoForm

# Create your views here.
def registro_vecino_views(request):
	formulario = AgregaVecinoForm()
	ctx = {'form': formulario}
	return render(request, 'registro/addVecino.html', ctx)