from django.shortcuts import render, redirect
from core.models import Producto
from core.forms import ProductoForm, CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate


# Create your views here.

def galeria(request):
    return render(request, 'core/galeria.html')

def home(request):
    return render(request, 'core/home.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def formulario(request):
    return render(request, 'core/formulario.html')

def quesoslacteos(request):
    return render(request, 'core/quesoslacteos.html')

def lacteos(request):
    return render(request, 'core/lacteos.html')

def quesos(request):
    return render(request, 'core/quesos.html')
@login_required
def listado_productos(request):
    productos = Producto.objects.all()
    data = {
        'productos':productos
    }
    return render(request, 'core/listado_productos.html', data)

@login_required
@permission_required('core.add_producto')
def nuevo_producto(request):
    data = {
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
    return render(request, 'core/nuevo_producto.html',data)
    
@permission_required('core.change_producto')
def modificar_producto(request, id):
    productos = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=productos)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=productos)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado correctamete"
        data['form'] = formulario
    return render(request, 'core/modificar_producto.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    productos = Producto.objects.get(id=id)
    productos.delete()
    return redirect(to="listado_productos")


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }
    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request,user)
            return redirect(to='home')


    return render(request, "registration/registrar.html", data)