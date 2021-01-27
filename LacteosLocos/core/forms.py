from django import forms
from django.forms import ModelForm,fields
from core.models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','fecha_elaboracion','fecha_caducidad','tipo']


class CustomUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
    
def clen_fecha_vencimiento(self):
    fecha1 = self.cleaned_data['fecha_elaboracion']
    fecha2 = self.cleaned_data['fecha_caducidad']

    if fecha1 > fecha2:
        raise forms.ValidationError("La fecha de elaboracion no puede ser mayor al vencimiento")
    return fecha1,fecha2