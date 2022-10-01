from __future__ import unicode_literals
from asyncio.windows_events import NULL
from codecs import unicode_escape_encode
from email import charset
from email.mime import image
from enum import unique
from operator import mod
import os
from pyexpat import model
from tabnanny import verbose
from typing import Set
from django import forms
from django.conf import settings
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from tkinter.tix import Tree
from turtle import update
from operator import truediv
from pydoc import describe

from numpy import unicode_
from CoopresolWeb.settings import MEDIA_ROOT

# Create your models here.



class Contactos(models.Model):
    Nombre = models.CharField(max_length=15)
    Apellido = models.CharField(max_length=15)
    Cedula = models.CharField(max_length=11,)   
    Direccion = models.CharField(max_length=240,)
    email = models.EmailField(verbose_name="Correo Electrónico")
    Telefono = models.CharField(max_length=10,blank=True,null=True)
    Celular = models.CharField(max_length=10,verbose_name='Teléfono Móvil')
    Patrocinador = models.CharField(max_length=240,null=True,blank=True)
    LugarNacimiento =models.CharField(max_length=240,verbose_name='Lugar De Nacimiento')
    FechaNacimiento =models.DateField(verbose_name='Fecha De Nacimiento',blank=True,null=True)
    edad = models.CharField(max_length=3,blank=True)
    Hijos = models.CharField(max_length=1)
    hijas = models.CharField(max_length=1)
    EstadoCivil = models.CharField(max_length=40,verbose_name='Estado Civil')
    LugarTrabajo= models.CharField(max_length=100,verbose_name='Empresa para La que Trabaja')
    TelTrabajo = models.CharField(max_length=10,verbose_name=' Teléfono De Lugar De trabajo')
    DireccionTrabajo = models.CharField(max_length=240,verbose_name='Dirección De Lugar De Trabajo')
    solicitud = models.FileField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Estado = models.CharField(max_length=240,verbose_name='Estado',default='ninguno')


 
    def __str__(self) :
        return self.Nombre
    
      

class SociosJuridicos(models.Model):
    NombreINS = models.CharField(max_length=40)
    TipoOrganizacion = models.CharField(max_length=40)
    RNC = models.CharField(max_length=11)
    Direccion = models.CharField(max_length=240,)
    email = models.EmailField(verbose_name="Correo Electrónico")
    Telefono = models.CharField(max_length=10,blank=True,null=True)
    Celular = models.CharField(max_length=10,verbose_name='Teléfono Móvil')
    WebSite = models.CharField(max_length=240,null=True,blank=True)
    PagoRealizado =models.CharField(max_length=240,verbose_name='Pago Realizado')
    solicitud = models.FileField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Estado = models.CharField(max_length=240,verbose_name='Estado',default='ninguno')

 
 
    def __str__(self) :
        return self.NombreINS


    # probando
    # def clean(self):
        # try:
           #  sc=SociosJuridicos.objects.get(
         #        RNC=self.cleaned_data['RNC'].upper()                
       #      )
     #        if not self.instace.pk:
   #              raise forms.ValidationError("registro ya existe")
 #            elif self.instance.pk!= sc.pk:
 #                raise forms.ValidationError("esta duplicado")
            
#         except SociosJuridicos.DoesNotExist:
#             pass
 #        return self.cleaned_data


        
class Proyectos(models.Model):
    Titulo = models.CharField(max_length=15)
    Portada = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    descripcion = models.TextField(max_length=340,default='')
    ImpactoEconomico = models.CharField(max_length=240,default='ninguno',verbose_name="Impacto Económico")
    ImpactoSocial = models.CharField(max_length=240,verbose_name="Impacto Social")
    IMpactoMedioAmbiental = models.CharField(max_length=240,blank=True,null=True,verbose_name="Impacto medioambiental")
    CapitalInvertido = models.CharField(max_length=10,verbose_name='Capital Invertido',default='')
    TiempoEjecucion = models.CharField(max_length=240,null=True,blank=True,verbose_name="Tiempo De Ejecucion")
    Duracion = models.CharField(max_length=240,verbose_name='Duracion',default='ninguno')
    Imagen1 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen2 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen3 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen4 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)

 
    def __str__(self) :
        return self.Titulo


class Ideas(models.Model):
    Titulo = models.CharField(max_length=15)
    descripcion = models.TextField(max_length=340,default='')
    ImpactoSocial = models.CharField(max_length=240,verbose_name="Impacto Social")
    IMpactoMedioAmbiental = models.CharField(max_length=240,blank=True,null=True,verbose_name="Impacto medioambiental")
    CapitalInvertido = models.CharField(max_length=10,verbose_name='Capital Invertido',default='')
    Duracion = models.CharField(max_length=240,verbose_name='Duracion',default='ninguno')
    Imagen1 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen2 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen3 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Imagen4 = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240)
    Nombre = models.TextField(max_length=340,default='')
    Apellido = models.TextField(max_length=340,default='')
    Telefono = models.TextField(max_length=11,default='')
    Correo = models.TextField(max_length=340,default='')

 
    def __str__(self) :
        return self.Titulo



class Equipo(models.Model):
    Nombre = models.CharField(max_length=45)
    Apellido = models.CharField(max_length=40)
    Role =models.CharField(max_length=45)
    HistorialProfesional =models.TextField(max_length=750,verbose_name='Historial Profesional')
    FotoPerfil = models.ImageField(upload_to=MEDIA_ROOT,default='tierra.jpg',null=True,max_length=240,verbose_name='Foto')


    
 
    def __str__(self) :
        return self.Nombre


class categoria(models.Model):
    Categoria =models.CharField(max_length=45)
    Subcategoria =models.CharField(max_length=750,blank=True,null=True)
 
    def __str__(self) :
        return self.Categoria


class Link(models.Model):
    Titulo = models.CharField(max_length=45)
    VideoURL = models.CharField(max_length=250)
    Categoria =  models.ForeignKey(categoria,on_delete=models.SET_NULL,null=True)
    
 
    def __str__(self) :
        return self.Titulo


class Correo(models.Model):
    Nombre = models.CharField(max_length=45,verbose_name='Nombre')
    Apellido = models.CharField(max_length=50,verbose_name='Apellido')
    Correo = models.EmailField(max_length=45,verbose_name='Correo Electrónico')
    Telefono = models.CharField(max_length=11,verbose_name='Teléfono')
    Asunto =models.CharField(max_length=75,verbose_name='Asunto')
    Mensaje = models.TextField(max_length=340,default='',verbose_name='Mensaje')
    Estado = models.CharField(max_length=240,verbose_name='Estado',default='Pendiente')

 
    def __str__(self) :
        return self.Nombre

        

