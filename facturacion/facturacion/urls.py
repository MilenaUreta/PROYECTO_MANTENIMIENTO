"""facturacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from man_factura.views import ventas,listar_productos,listar_clientes,producto,editarprod,cliente,editarcliente,eliminarproducto,eliminarcliente
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ventas,name='index'),
    path('ventas/',ventas,name='index'),
    path('productos/',listar_productos,name='productos'),
    path('clientes/',listar_clientes,name='clientes'),
    path('producto/',producto,name='producto'),
    path('editprod/<int:id>',editarprod,name='editarproducto'),
    path('cliente/',cliente,name='cliente'),
    path('editcli/<int:id>',editarcliente,name='editarcliente'),
    path('eliminprod/<int:id>',eliminarproducto,name='eliminarprod'),
    path('elimincli/<int:id>',eliminarcliente,name='eliminarcliente'),
   


]
