from cProfile import label
from dataclasses import fields
from pyexpat import model
from statistics import mode
from tkinter import Label
from xml.dom.minidom import Attr
from django.conf import settings
from django.forms import ModelForm
from .models import Contactos,Proyectos,Equipo,Link,categoria,Correo,Ideas,SociosJuridicos
from administracion.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#from tkinter import*


class FormContactos(ModelForm):
    class Meta:

        model = Contactos
        fields = '__all__'
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}),
            'Patrocinador': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Patrocinador(opcional'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Apellido'}),
            'Cedula': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Cédula'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Dirección'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Correo Electrónico'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Teléfono '}),
            'Celular': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Celular'}),
            'LugarNacimiento': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Lugar De Nacimiénto'}),
            'edad': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Edad'}),
            'Hijos': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Híjos(cantidad)'}),
            'hijas': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Híjas(cantidad)'}),
            'EstadoCivil': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Estado Civil'}),
            'LugarTrabajo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Lugar De Trabajo'}),
            'TelTrabajo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Teléfono Lugar De Trabajo'}),
            'DireccionTrabajo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Dirección Lugar De Trabajo'}),

            'solicitud': forms.FileInput(attrs={'id':'formFile'}), 
            
            'FechaNacimineto': forms.DateField(input_formats=settings.DATE_INPUT_FORMATS),
            'FechaNacimiento': forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY' ,'class':'form-control'}),
            
            
            
        }

class formPerJuridcica(ModelForm):
    class Meta:

        model = SociosJuridicos
        fields = '__all__'
        exclude=['PagoRealizado','Estado']
        widgets = {
            'NombreINS': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}),
            'TipoOrganizacion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tipo De Organización'}),
            'RNC': forms.TextInput(attrs={'class': 'form-control','placeholder': 'RNC'}),
            'Direccion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Dirección'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Correo Electrónico'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Teléfono'}),
            'Celular': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Celular'}),
            'WebSite': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Sitio Web'}),
            'PagoRealizado': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Pago Realizado'}),
            'solicitud': forms.FileInput(attrs={'id':'formFile'}), 
               
        }


class FormProyectos(ModelForm):
    class Meta:

        model = Proyectos
        fields = '__all__'
        
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'Portada': forms.FileInput(attrs={'class': 'form-control'}),
            'ImpactoEconomico': forms.TextInput(attrs={'class': 'form-control'}),
            'ImpactoSocial': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),

            'IMpactoMedioAmbiental': forms.TextInput(attrs={'class': 'form-control'}),

            'CapitalInvertido': forms.TextInput(attrs={'class': 'form-control'}),
            'TiempoEjecucion': forms.TextInput(attrs={'class': 'form-control'}),
            'Duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'Imagen1': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen2': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen3': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen4': forms.FileInput(attrs={'class': 'form-control'}),

            
            
         }


class FormIdeas(ModelForm):
    class Meta:

        model = Ideas
        fields = '__all__'
        
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'ImpactoSocial': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'IMpactoMedioAmbiental': forms.TextInput(attrs={'class': 'form-control'}),
            'CapitalInvertido': forms.TextInput(attrs={'class': 'form-control'}),
            'Duracion': forms.TextInput(attrs={'class': 'form-control'}),
            'Imagen1': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen2': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen3': forms.FileInput(attrs={'class': 'form-control'}),
            'Imagen4': forms.FileInput(attrs={'class': 'form-control'}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'Correo': forms.TextInput(attrs={'class': 'form-control'}),
            
            
         }



class FormLINKS(ModelForm):
    class Meta:

        model = Link
        fields = '__all__'
        widgets = {
            'Titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'VideoURL': forms.TextInput(attrs={'class': 'form-control'}),
            'Categoria': forms.Select(attrs={'class': 'form-control'}),
            

            
        } 
    
class FormCategoria(ModelForm):
    class Meta:

        model = categoria
        fields = '__all__'
        widgets = {
            'Titulo': forms.Textarea(attrs={'class': 'form-control'}),
            'Subcategoria': forms.TextInput(attrs={'class': 'form-control'}),
            'Categoria': forms.TextInput(attrs={'class': 'form-control'}),
            

            
        }   

class formEquipo(ModelForm):
    class Meta:

        model = Equipo
        fields = '__all__'
        widgets = {
            'HistorialProfesional': forms.Textarea(attrs={'class': 'form-control','rows':5}),
            'Nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'Apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'Role': forms.TextInput(attrs={'class': 'form-control'}),

            
        }    
        
class FormCorreo(ModelForm):
    class Meta:

        model = Correo
        exclude=['Estado']
        fields = '__all__'
# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Image
#         fields = ('title', 'image')


class creaciondeusuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'sadadasd': forms.PasswordInput()
            
        } 


class FormUsuario(ModelForm):
    class Meta:

        model = User
        fields = ['username','email','password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control me-2','placeholder': 'Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'password': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}),
            

            
        } 