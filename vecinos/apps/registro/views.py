from django.shortcuts import render, redirect
from vecinos.apps.registro.forms import AgregaVecinoForm, AgregaCalleForm
from vecinos.apps.registro.models import Calle, Vecino, Casa

def index_views(request):
	return render(request, 'registro/index.html')

def registro_vecino_views(request):
	if request.POST.get("Aceptar"):
		form = AgregaVecinoForm(request.POST, request.FILES)
		if form.is_valid():
				calle = form.cleaned_data['calle']
				numero = form.cleaned_data['numero']
				telefono = form.cleaned_data['telefono']
				nombre = form.cleaned_data['nombre']
				v = Vecino.objects.filter(telefono=telefono)
				c = Calle.objects.filter(calle=calle)[0]
				casa = Casa.objects.filter(numero=numero, calle=c)
				if not v:
					vec = Vecino()
					vec.nombre = nombre
					vec.telefono = telefono
					if not casa:
						ca = Casa()
						ca.calle = c
						ca.numero = numero
						ca.save()
						vec.casa = ca
					else:
						vec.casa = casa[0]
					vec.save()
				return redirect(listado_vecinos_views)
	else:
		formulario = AgregaVecinoForm()
		ctx = {'form': formulario}
		return render(request, 'registro/addVecino.html', ctx)

def registro_calle_views(request):
	if request.POST.get("Aceptar"):
		calle = AgregaCalleForm(request.POST, request.FILES)
		if calle.is_valid():
			calleNueva = calle.cleaned_data['calle']
			c = Calle.objects.filter(calle=calleNueva)
			if not c:
				ca = Calle()
				ca.calle = calleNueva
				ca.save()
				return redirect(listado_calles_views)
	else:
		formulario = AgregaCalleForm()
		ctx = {'form': formulario}
		return render(request, 'registro/addCalle.html', ctx)

def listado_calles_views(request):
	calles = Calle.objects.all()
	ctx = {'tabla': calles}
	return render(request, 'registro/listadoCalles.html', ctx)

def listado_vecinos_views(request):
	vecinos = Vecino.objects.all()
	ctx = {'tabla': vecinos}
	return render(request, 'registro/listadoVecinos.html', ctx)

