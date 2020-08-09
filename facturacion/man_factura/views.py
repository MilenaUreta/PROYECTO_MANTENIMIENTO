from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Cliente,Producto,Factura,DetalleFactura
from .forms import ProductoForm,clienteform

def ventas(request): 
    queryset= request.GET.get('buscar')
    if queryset:
        facturas=Factura.objects.filter(
            Q(cliente__nombre__icontains= queryset)|
            Q(id__icontains= queryset)
            )
        opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','fact':facturas}
        return render(request, 'index.html', opciones)
    facturas=Factura.objects.all()
    opciones = {'Ventas': 'Ventas',
            'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','fact':facturas}
    return render(request, 'index.html', opciones)

def listar_productos(request): 
    queryset= request.GET.get('buscar')
    if queryset:
        producto=Producto.objects.filter(
            Q(descripcion__icontains= queryset)|
            Q(id__icontains= queryset)
            )
        opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','prod':producto}
        return render(request, 'listar_productos.html', opciones)
    producto= Producto.objects.all()   
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','prod':producto}
    return render(request, 'listar_productos.html', opciones)



def listar_clientes(request): 
    queryset= request.GET.get('buscar')
    if queryset:
        clientes=Cliente.objects.filter(nombre__icontains= queryset)
        opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','cli':clientes}
        return render(request, 'listar_clientes.html', opciones)
    Clientes= Cliente.objects.all()   
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','cli':Clientes}
    return render(request, 'listar_clientes.html', opciones)


def producto(request):
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','accion':'Agregar'}
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('productos')
    else:
        form=ProductoForm()
        opciones['form'] = form
    return render(request,'producto.html',opciones)




def editarprod(request, id):
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','accion':'Actualizar'}
    producto = Producto.objects.get(id=id)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
        opciones['form'] = form
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')

    return render(request, 'producto.html', opciones)


def cliente(request):
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','accion':'Agregar'}
    if request.method=='POST':
        form=clienteform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('clientes')
    else:
        form=clienteform()
        opciones['form'] = form
    return render(request,'cliente.html',opciones)

def editarcliente(request, id):
    opciones = {'Ventas': 'Ventas',
                'Productos': 'Productos', 'Clientes': 'Clientes','Admin':'Administrador','accion':'Actualizar'}
    producto = Cliente.objects.get(id=id)
    if request.method == 'GET':
        form = clienteform(instance=producto)
        opciones['form'] = form
    else:
        form = clienteform(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('clientes')

    return render(request, 'cliente.html', opciones)


def eliminarproducto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})



def eliminarcliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'eliminar_cliente.html', {'cliente': cliente})