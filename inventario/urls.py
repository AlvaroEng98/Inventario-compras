from django.urls import path

from .models import Element
from .views import  ElementListView, ElementDeleteView, ElementDetailView, ValeVentaDeleteView, listar_ventas_vale, \
    VentasDeleteView, VentasDetailView, listar_compras_vale, ComprasDeleteView, ComprasDetailView, create_elemet, \
    create_compras, create_venta, edit_elemento,OperacionesListView, ValeCompraListView, create_vale_compra,  \
    ValeVentaListView,create_vale_venta, edit_venta ,edit_compra,OperacionesDeleteView,ComprasDeleteView, ValeCompraDeleteView

urlpatterns = [
    path("", OperacionesListView.as_view(), name="home"),
    path("delete-operaciones/<int:id_operacion>",OperacionesDeleteView.as_view(), name="delete_operacion"),
    #url relativas para los vales de venta

    path("vales-venta", ValeVentaListView.as_view(), name="vales_venta_list"),
    path("vales-venta/crear", create_vale_venta, name="vales_venta_create"),
    path("vales-venta/<int:pk>/eliminar", ValeVentaDeleteView.as_view(), name='vale_venta_delete'),
    #url relativas para los vales de compra
    path("vales-compra", ValeCompraListView.as_view(), name="vales_compra_list"),
    path("vales-compra/crear", create_vale_compra, name="vales_compra_create"),
    path("vales-compra/<int:pk>/eliminar", ValeCompraDeleteView.as_view(), name='vale_compra_delete'),

    #urls relativas con los elementos
    path("elementos", ElementListView.as_view(), name="elementos_list"),
    path("elementos/insertar", create_elemet, name="create_element"),
    path("elementos/eliminar/<int:pk>", ElementDeleteView.as_view(), name="elementos_delete"),
    path("elementos/editar/<int:element_id>", edit_elemento, name="elementos_edit"),
    path("elementos/detalles/<int:pk>", ElementDetailView.as_view(), name="elementos_detail"),

    #urls relativas a las ventas
    path("vales-venta/<int:vale_venta_id>/listado_ventas", listar_ventas_vale, name="ventas_list"),
    path("vales-venta/<int:vale_venta_id>/insertar", create_venta, name="create_venta"),
    path("vales-venta/<int:vale_venta_id>/eliminar/<int:pk>", VentasDeleteView.as_view(), name="ventas_delete"),
    path("vales-venta/<int:vale_venta_id>/editar/<int:venta_id>", edit_venta, name="ventas_edit"),
    path("vales-venta/<int:vale_venta_id>/detalles/<int:pk>", VentasDetailView.as_view(), name="ventas_details"),

    #urls relativas para las compras
    path("vales-compra/<int:vale_compra_id>/listado-compras", listar_compras_vale, name="compras_list"),
    path("vales-compra/<int:vale_compra_id>/insertar", create_compras, name="create_compras"),
    path("vales-compra/<int:vale_compra_id>/eliminar/<int:pk>", ComprasDeleteView.as_view(), name="compras_delete"),
    path("vales-compra/<int:vale_compra_id>/editar/<int:compra_id>", edit_compra, name="compras_edit"),
    path("vales-compra/<int:vale_compra_id>/detalles/<int:pk>", ComprasDetailView.as_view(), name="compras_detail"),





]