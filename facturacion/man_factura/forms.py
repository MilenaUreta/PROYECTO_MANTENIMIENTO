from django import forms
from .models import Producto,Cliente
class ProductoForm(forms.ModelForm):

    class Meta():
        model=Producto
        fields = ('descripcion', 'precio', 'stock','iva')
        # labels = {'descripcion': 'Descripcion', 'precio': 'Precio', 'stock': 'Stock','iva':'Iva'}
        widgets={
             'descripcion': forms.TextInput(attrs={'class':'form-control ','type':'text','id':'descripcion', 'placeholder':'descripcion'}),
             'precio':forms.TextInput(attrs={'class':'form-control ','type':'number','id':'precio'}),
             'stock':forms.TextInput(attrs={'class':'form-control ','type':'number','id':'stock'}),  
        }
        

class clienteform(forms.ModelForm):
    class Meta():
        model=Cliente
        fields = ('ruc', 'nombre', 'correo','telefono','direccion')
        # labels = {'ruc': 'Ruc', 'nombre': 'Nombre', 'correo': 'Mail','telefono':'Telefono','direccion':'Direccion'}
        widgets={
             'ruc': forms.TextInput(attrs={'class':'form-control ','type':'number','id':'ruc'}),
             'nombre':forms.TextInput(attrs={'class':'form-control ','type':'text','id':'nombre'}),
             'correo':forms.EmailInput(attrs={'class':'form-control ','type':'email','id':'correo','placeholder':'example@dominio.com'}),  
             'telefono':forms.NumberInput(attrs={'class':'form-control ','type':'number','id':'telefono'}),
             'direccion': forms.Textarea(attrs={'class':'form-control ','style':"width:50 ; height:100px ;",'type':'textarea','id':'direccion','placeholder':'Direccion'}),
        }
        





