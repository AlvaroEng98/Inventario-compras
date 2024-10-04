from django.urls import path

from .models import Element
from .views import  ElementListView, ElementDeleteView, ElementDetailView, VentasListView, \
    VentasDeleteView, VentasDetailView, ComprasListView, ComprasDeleteView, ComprasDetailView, create_elemet, \
    create_compras, create_venta, edit_elemento,OperacionesListView, ValeCompraListView, create_vale_compra, ValeVentaListView,create_vale_venta 

urlpatterns = [
    path("", OperacionesListView.as_view(), name="home"),
    #url relativas para los vales de venta

    path("vales-venta", ValeVentaListView.as_view(), name="vales_venta_list"),
    path("vales-venta/crear", create_vale_venta, name="vales_venta_create"),

    #url relativas para los vales de compra
    path("vales-compra", ValeCompraListView.as_view(), name="vales_compra_list"),
    path("vales-compra/crear", create_vale_compra, name="vales_compra_create"),

    #urls relativas con los elementos
    path("elementos/insertar", create_elemet, name="create_element"),
    path("elementos", ElementListView.as_view(), name="elementos_list"),
    path("elementos/eliminar/<int:pk>", ElementDeleteView.as_view(), name="elementos_delete"),
    path("elementos/editar/<int:pk>", edit_elemento, name="elementos_edit"),
    path("elementos/detalles/<int:pk>", ElementDetailView.as_view(), name="elementos_detail"),

    #urls relativas a las ventas
    path("ventas/insertar", create_venta, name="create_venta"),
    path("ventas", VentasListView.as_view(), name="ventas_list"),
    path("ventas/eliminar/<int:pk>", VentasDeleteView.as_view(), name="ventas_delete"),
    path("ventas/editar/<int:pk>", VentasDetailView.as_view(), name="ventas_edit"),

    #urls relativas para las compras
    path("compras/insertar", create_compras, name="create_compras"),
    path("compras", ComprasListView.as_view(), name="compras_list"),
    path("compras/eliminar/<int:pk>", ComprasDeleteView.as_view(), name="compras_delete"),
    path("compras/detalles/<int:pk>", ComprasDetailView.as_view(), name="compras_detail"),





]