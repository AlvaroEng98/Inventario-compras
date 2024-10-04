from django.urls import path

from .models import Element
from .views import  ElementListView, ElementDeleteView, ElementDetailView, VentasListView, \
    VentasDeleteView, VentasDetailView, ComprasListView, ComprasDeleteView, ComprasDetailView, create_elemet, \
    create_compras, create_venta, edit_elemento,OperacionesListView, ValeCompraListView, create_vale_compra,  \
    ValeVentaListView,create_vale_venta, edit_venta ,edit_compra,OperacionesDeleteView

urlpatterns = [
    path("", OperacionesListView.as_view(), name="home"),
    path("delete-operaciones/<int:pk>",OperacionesDeleteView.as_view(), name="delete_operacion"),
    #url relativas para los vales de venta


    path("vales-venta", ValeVentaListView.as_view(), name="vales_venta_list"),
    path("vales-venta/crear", create_vale_venta, name="vales_venta_create"),

    #url relativas para los vales de compra
    path("vales-compra", ValeCompraListView.as_view(), name="vales_compra_list"),
    path("vales-compra/crear", create_vale_compra, name="vales_compra_create"),

    #urls relativas con los elementos
    path("elementos", ElementListView.as_view(), name="elementos_list"),
    path("elementos/insertar", create_elemet, name="create_element"),
    path("elementos/eliminar/<int:pk>", ElementDeleteView.as_view(), name="elementos_delete"),
    path("elementos/editar/<int:pk>", edit_elemento, name="elementos_edit"),
    path("elementos/detalles/<int:pk>", ElementDetailView.as_view(), name="elementos_detail"),

    #urls relativas a las ventas
    path("ventas", VentasListView.as_view(), name="ventas_list"),
    path("ventas/insertar", create_venta, name="create_venta"),
    path("ventas/eliminar/<int:pk>", VentasDeleteView.as_view(), name="ventas_delete"),
    path("ventas/editar/<int:pk>", edit_venta, name="ventas_edit"),
    path("ventas/detalles/<int:pk>", VentasDetailView.as_view(), name="ventas_details"),

    #urls relativas para las compras
    path("vales-compra/<int:pk>/listado-compras", ComprasListView.as_view(), name="compras_list"),
    path("vales-compra/<int:pk>/insertar", create_compras, name="create_compras"),
    path("vales-compra/<int:pk>/eliminar/<int:pk>", ComprasDeleteView.as_view(), name="compras_delete"),
    path("compras/editar/<int:pk>", edit_compra, name="compras_edit"),
    path("compras/detalles/<int:pk>", ComprasDetailView.as_view(), name="compras_detail"),





]