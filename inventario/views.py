from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, DetailView

from inventario.models import Compra, Element, Venta


# Create your views here.

#metodos relacionados con la creacion, edicion, eliminacion -- no hace falta, listar y visualizar una comprar/venta
#metodos relacionados con el listado del inventario y las operaciones

#posivilidad de analizis a lo largo del mes de lo mas vendido y lo que mas urgente es comprar

class HomePageView(TemplateView):
    template_name = "home.html"

def create_venta(request):

    elemetos = Element.objects.all()
    if request.method == 'POST':

        venta = Venta()
        venta.fecha_venta = request.POST['fecha_venta']
        venta.cantidad =request.POST['cantidad']
        venta.elemento = request.POST['elemento']
        venta.save()

        return redirect('ventas_list', {})
    return render(request,r'ventas/ventas_create.html', {'elemetos': elemetos})

class VentasListView(ListView):
    model = Venta
    template_name = r"ventas/ventas_list.html"

class VentasDetailView(DetailView):
    model = Venta
    template_name = r"ventas/ventas_details.html"

class VentasDeleteView(DeleteView):
    model = Venta
    template_name = r"ventas/ventas_delete.html"
    success_url = reverse_lazy("")

def create_compras(request):
    elemetos = Element.objects.all()
    if request.method == 'POST':
        cantidad = request.POST['cantidad']
        fecha_compra = request.POST['fecha_compra']
        fecha_compra = datetime.strptime(fecha_compra, '%m/%d/%Y').strftime('%Y-%m-%d')
        elemento_nombre = request.POST['elemento']
        try:
            elemento = Element.objects.get(nombre=elemento_nombre)
        except Element.DoesNotExist:
            return render(request, r'compras/compras_create.html', {'elemetos': elemetos, 'error': 'Elemento no encontrado'})
        compra = Compra()
        compra.fecha_compra = fecha_compra
        compra.cantidad = cantidad
        compra.elemento = elemento
        compra.save()
        return redirect('compras_list')
    return render(request, r'compras/compras_create.html', {'elemetos': elemetos})


class ComprasListView(ListView):
    model = Compra
    template_name = r"compras/compras_list.html"

class ComprasDeleteView(DeleteView):
    model = Compra
    template_name = r"compras/compra_delete.html"
    success_url = reverse_lazy("elementos_list")


class ComprasDetailView(DetailView):
    model = Compra
    template_name = r"compras/compra_details.html"

#template para crear nueva compra

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


