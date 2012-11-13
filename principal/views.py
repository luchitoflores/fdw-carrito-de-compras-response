from principal.models import Recambio, CarritoDeCompra
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import modelformset_factory


def lista_recambios(request):
    lista_recambios = Recambio.objects.all()
    return render_to_response('lista_recambios.html', {
        'lista_recambios': lista_recambios
    }, context_instance=RequestContext(request))


def carrito_de_compra(request, id_item=None):
    carrito_de_compra = CarritoDeCompra.objects.all()

    precio_total = 0
    unidades_totales = 0
    for recambio in carrito_de_compra:
        precio_total = recambio.precio * recambio.unidades + precio_total
        unidades_totales = recambio.unidades + unidades_totales

    UnidadesFormSet = modelformset_factory(CarritoDeCompra, extra=0)
    if request.method == 'POST':
        post = request.POST
        formset = UnidadesFormSet(post)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect('/carrito-de-compra/')
    else:
        if id_item:
            item_to_erase = CarritoDeCompra.objects.get(pk=id_item)
            item_to_erase.delete()
            item_to_erase = None
            return HttpResponseRedirect('/carrito-de-compra/')
        else:
            formset = UnidadesFormSet(queryset=carrito_de_compra)

    return render_to_response('carrito_de_compra.html', {
        'carrito_de_compra': carrito_de_compra,
        'precio_total': precio_total,
        'unidades_totales': unidades_totales,
        'formset': formset
    }, context_instance=RequestContext(request))
