from django.shortcuts import render, redirect, get_object_or_404
from vecinos.apps.registro.forms import CasaForm
from vecinos.apps.registro.models import Calle, Casa, Like, Prevision, TipoBono, BonoPrevision
from django.utils.text import slugify
from django.http import HttpResponseRedirect, HttpResponseServerError
from django.http import HttpResponse


def calles(request):
    print("este")
    fonasa = Prevision.objects.get(nombre='Fonasa')
    papel = TipoBono.objects.get(tipo_bono='Papel')
    rel1 = BonoPrevision(bono=papel, prevision=fonasa)
    rel1.save()
    print('rel', rel1)
    calles = Calle.objects.all()
    return render(request, 'registro/calles.html', {'calles': calles})


def like_calles(request):
    if request.method == 'GET':
        id_calle = request.GET['id_calle']
        calle_liked = Calle.objects.get(pk=id_calle)
        m = Like(like=calle_liked)
        m.save()
        return HttpResponse("success!!")
    else:
        return HttpResponse("no es GET")


def create_calle(request):
    error_msj = "No hay datos"
    if request.method == 'POST':
        calle = request.POST.copy()
        if calle.get('calle'):
            calleNueva = calle['calle']
            slugNueva = slugify(calleNueva)
            if Calle.objects.filter(slug=slugNueva).count() > 0:
                error_msj = "calle ya existe"
            else:
                ca = Calle(calle=calleNueva, slug=slugNueva)
                ca.save()
                return HttpResponseRedirect(ca.get_absolute_url())
        else:
            error_msj = "Campo obligatorio"
    return HttpResponseServerError(error_msj)


def update_calle(request, slug):
    if request.method == "POST":
        post = request.POST.copy()
        calle = Calle.objects.get(slug=slug)
        if post.get('calle'):
            slugNueva = slugify(post.get('calle'))
            if slug != slugNueva and \
               Calle.objects.filter(slug=slugNueva).count() > 0:
                error_msg = "calle ya existe."
                return HttpResponseServerError(error_msg)
            calle.slug = slugNueva
            calle.calle = post['calle']
            calle.save()
            return HttpResponseRedirect('/listCalles/')
    error_msg = "No POST data sent."
    return HttpResponseServerError(error_msg)


def list_casa(request, template_name="registro/casa_list.html"):
    casas = Casa.objects.all()
    return render(request, template_name, {'object_list': casas})


def create_casa(request, template_name="registro/casa_form.html"):
    if request.method == "GET":
        print("entra a get")
        form = CasaForm()
    else:
        print("entra a POST")
        form = CasaForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(list_casa)
    return render(request, template_name, {'form': form})


def update_casa(request, id, template_name="registro/casa_form.html"):
    casa = get_object_or_404(Casa, pk=id)
    form = CasaForm(request.POST or None, instance=casa)
    if form.is_valid():
        form.save()
        return redirect(list_casa)
    return render(request, template_name, {'form': form})


def delete_casa(request, id,
                template_name="registro/casa_confirm_delete.html"):
    casa = get_object_or_404(Casa, pk=id)
    if request.method == "POST":
        casa.delete()
        return redirect(list_casa)
    return render(request, template_name, {'object': casa})
