
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DeleteView, DetailView
from django.dispatch import receiver
from inventario.models import Compra, Element, Venta, Operacion, Vale_venta, Vale_compra
from django.db.models.signals import post_save


# Create your views here.

#metodos relacionados con la creacion, edicion, eliminacion -- no hace falta, listar y visualizar una comprar/venta
#metodos relacionados con el listado del inventario y las operaciones

#posivilidad de analizis a lo largo del mes de lo mas vendido y lo que mas urgente es comprar


class OperacionesListView(ListView):
    model = Operacion
    template_name = 'home.html'

class OperacionesDeleteView(DeleteView):
    model = Operacion
    template_name = r"operaciones/operaciones_delete.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Venta'
        context['message'] = '¿Estás seguro de que deseas eliminar este registro?'
        return context

class ValeVentaListView(ListView):
    model = Vale_venta
    template_name = r'vales/listado_vales_ventas.html'

def create_vale_venta(request):
        
    vale_venta = Vale_venta()
    vale_venta.save()

    return redirect(reverse('vales_venta_list'))
    

class ValeCompraListView(ListView):
    model = Vale_compra
    template_name = r'vales/listado_vales_compras.html'

def create_vale_compra(request):

    vale_compra = Vale_compra()
    vale_compra.save()

    return redirect(reverse('vales_compra_list'))


def create_venta(request):

    elemetos = Element.objects.all()
    if request.method == 'POST':

        cantidad = request.POST['cantidad']
        elemento_nombre = request.POST['elemento']
        elemento = Element.objects.get(nombre=elemento_nombre)

        venta = Venta()
        venta.cantidad = cantidad
        venta.elemento = elemento    
  
        venta.ganancia = (elemento.precio_venta - elemento.precio_compra)*int(cantidad)
        venta.save()

        return redirect('ventas_list')
    return render(request,r'ventas/ventas_create.html', {'elemetos': elemetos})

def edit_venta(request, pk):
    
    elemetos = Element.objects.all()
    venta = get_object_or_404(Venta, pk = pk)

    if request.method == 'POST':

        cantidad = request.POST['cantidad']
        elemento_nombre = request.POST['elemento']
        elemento = Element.objects.get(nombre=elemento_nombre)

        venta.cantidad = cantidad
        venta.elemento = elemento
        venta.ganancia = (elemento.precio_venta - elemento.precio_compra)*int(cantidad)
        venta.save()
        
        return redirect('ventas_list')
    return render(request,r'ventas/ventas_edit.html', {'elemetos': elemetos})


class VentasListView(ListView):
    model = Venta
    template_name = r"ventas/ventas_list.html"


class VentasDetailView(DetailView):
    model = Venta
    template_name = r"ventas/ventas_details.html"

class VentasDeleteView(DeleteView):
    model = Venta
    template_name = r"ventas/ventas_delete.html"
    success_url = reverse_lazy("ventas_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Venta'
        context['message'] = '¿Estás seguro de que deseas eliminar esta venta?'
        return context


def create_compras(request):
    elemetos = Element.objects.all()
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        elemento_nombre = request.POST['elemento']
        elemento = Element.objects.get(nombre=elemento_nombre)

        compra = Compra()
        compra.cantidad = cantidad
        compra.elemento = elemento
        compra.inversion = elemento.precio_compra
    
        compra.save()
        return redirect('compras_list')
    return render(request, r'compras/compras_create.html', {'elemetos': elemetos})

def edit_compra(request, pk):

    elemetos = Element.objects.all()
    compra = get_object_or_404(Compra, pk = pk)

    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        elemento_nombre = request.POST['elemento']
        elemento = Element.objects.get(nombre=elemento_nombre)

        compra.cantidad = cantidad
        compra.elemento = elemento
        compra.inversion = elemento.precio_compra
    
        compra.save()
        return redirect('compras_list')
    return render(request, r'compras/compras_edit.html', {'elemetos': elemetos})



class ComprasListView(ListView):
    model = Compra
    template_name = r"compras/compras_list.html"

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Compra.objects.filter(vale_compra_id=pk)


class ComprasDeleteView(DeleteView):
    model = Compra
    template_name = r"compras/compra_delete.html"
    success_url = reverse_lazy("compras_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Compra'
        context['message'] = '¿Estás seguro de que deseas eliminar esta compra?'
        return context

class ComprasDetailView(DetailView):
    model = Compra
    template_name = r"compras/compra_details.html"

class ElementListView(ListView):
    model = Element
    template_name = r"elementos/elementos_list.html"

class ElementDeleteView(DeleteView):
    model = Element
    template_name = r"elementos/elementos_delete.html"
    success_url = reverse_lazy('elementos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Elemento'
        context['message'] = '¿Estás seguro de que deseas eliminar este elemento?'
        return context

class ElementDetailView(DetailView):
    model = Element
    template_name = r"elementos/elementos_details.html"

def create_elemet(request):

    if request.method == 'POST':

        element = Element()
        element.nombre = request.POST['nombre']
        element.precio_compra = request.POST['precio_compra']
        try:
            element.precio_venta = int(request.POST.get('precio_venta', 0))
        except ValueError:
            element.precio_venta = 0
        #ejecutar con un login, pero un login de verdad
        element.save()

        return redirect("elementos_list")
    return render(request, 'elementos/elementos_create.html',{})

def edit_elemento(request, pk ):

    elemento = get_object_or_404(Element, pk = pk)

    if request.method == 'POST':

        elemento.nombre = request.POST['nombre']
        elemento.precio_compra = request.POST['precio_compra']
        elemento.precio_venta = request.POST['precio_venta']
        elemento.save()

        return redirect("elementos_list")

    return render(request, 'elementos/elementos_create.html',{'elemento':elemento})


#signal para que cuando se cree una compra o una venta 
#funcion para cuando se cree una venta
@receiver(post_save, sender=Vale_compra)
def mi_retroalimentacion(sender, instance, created, **kwargs):
    if created:

        operacion = Operacion()
        operacion.operacion = 'Compra'
        operacion.cantidad = instance.inversion_total
        operacion.save()

#funcion para cuando se cree una compra
@receiver(post_save, sender=Vale_venta)
def mi_retroalimentacion(sender, instance, created, **kwargs):
    if created:

        operacion = Operacion()
        operacion.operacion = 'Venta'
        operacion.cantidad = instance.ganancia_total
        operacion.save()
