from base64 import encode
from distutils.log import error
from multiprocessing import context
import sqlite3
from django.http import BadHeaderError, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.files import File
from CoopresolWeb.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL, STATICFILES_DIRS
from .models import Contactos, Ideas,Proyectos,Equipo,Link,categoria,Correo,SociosJuridicos
from inicio import formulario
from .formulario import FormCategoria, FormContactos, FormProyectos, formEquipo,FormCorreo,FormIdeas,formPerJuridcica
from datetime import date, datetime
from fpdf import FPDF
import pyodbc
import pypyodbc
from django.conf import settings as django_settings
import os
from django.db.models import Q
from os.path import join
from django.core.mail import send_mail
from django.core import mail
from urllib import request, parse
# Create your views here.

salas=[
    {'id':1,'nombre':'python'},
    {'id':2,'nombre':'java'},
    {'id':3,'nombre':'c#'}
]

def Inicio(request):
        
       
        proyectos = Proyectos.objects.all()
        link = [
        'https://www.youtube.com/embed/7HJ5jd0mMCI',
        'https://www.youtube.com/embed/7HJ5jd0mMCI',
        'https://www.youtube.com/embed/7HJ5jd0mMCI' 
        ]
        context = {
                'proyectos':proyectos
        }
        return render(request,'inicio/inicio.html',context)


def Asociate(request):
    contactos = Contactos.objects.all()    
    formulario = FormContactos()
    formularioJuridica = formPerJuridcica()
    if request.method == "POST":
        hoy = date.today()
        lafecha = request.POST.get('FechaNacimiento')
        fecha = datetime.strptime(lafecha, '%d/%m/%Y')
        uno_o_cero = ((hoy.month, hoy.day) < (fecha.month, fecha.day))

        anios_de_diferencia = hoy.year - fecha.year
        edad = anios_de_diferencia - uno_o_cero
        
        request.POST._mutable = True
        request.POST['edad'] = edad
        request.POST['FechaNacimiento'] = fecha
        
 # creacion y guardad de solicitud en forma de pdf:
        
        pdf = FPDF() # crear variable de librearia fpdf que sirve para crear archivos pdf y en escrbir datos en estos
 

        pdf.add_page()# agrargar pagina
 
        # Establecer el estilo en tamaño de fondo que desees
        pdf.set_font("Arial", size = 15)
        th = pdf.font_size
# crear celdas o lineas

        #esto es una linead entre los parametros estan el texto que queremos en esta linea 
        #la alineacion(justificacion)
        #cuantas lineas ocupa
        if request.method == 'POST':
                

                pdf.cell(200, 10, txt = "Coopresol",
                        ln = 1, align = 'C')
                pdf.ln(th)
        #aquie termina la declaracion de la primera linea las siguientes lineas estan a continuacion:

                pdf.image( MEDIA_ROOT+"/static/media/avada-charity-logo-retina.png", x = 52, y = None, w = 100, h =20, type = '')

                pdf.cell(200, 10, txt = "Solicitud para Asociarse A la Cooperativa",
                        ln = 1, align = 'C')
                pdf.ln(th)
                ##########################################
                pdf.cell(190, 10, txt = "NOMBRE: "+request.POST.get('Nombre') +' '+request.POST.get('Apellido'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = "FECHA DE NACIMINETO: "+str(request.POST.get('FechaNacimiento')) +'   ' +"Nacionalidad: Pendiente",
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'SEXO: Pendiente '+'ESTADO CIVIL: '+request.POST.get('EstadoCivil'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'DIRECCION: '+request.POST.get('Direccion'),
                        ln = 1, align = 'l',border=1)  
                ##########################################     
                pdf.cell(190, 10, txt = 'CORRECO ELECTRONICO: '+request.POST.get('email'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'TELEFONO: '+request.POST.get('Telefono'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'TELEFONO MOVIL: '+request.POST.get('Celular'),
                        ln = 1, align = 'l',border=1)
                pdf.cell(190, 10, txt = 'PATROCINADOR: '+request.POST.get('Patrocinador'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'LUGAR DE NACIMINETO: '+request.POST.get('LugarNacimiento'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'HIJOS '+request.POST.get('Hijos') + 'HIJAS: '+request.POST.get('hijas'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'EMPRES PARA LA QUE TRABAJA: '+request.POST.get('LugarTrabajo'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'TELEFONO DE LUGAR DE TRABAJO: '+request.POST.get('TelTrabajo'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'DIRECCION DE LUGAR DE TRABAJO: '+request.POST.get('DireccionTrabajo'),
                        ln = 1, align = 'l',border=1)
                pdf.cell(190, 10, txt = 'static/media/solicitudes/Solicitud-'+request.POST.get('Nombre')+'_'+request.POST.get('Apellido')+'.pdf',
                        ln = 1, align = 'l',border=1)
# Guardar el archivo con estencoin en pdf en el directorio de static que es directorio base donde django
# trata con archivos estaticos, en este caso uso el mismo request para extraer el nombre y apellido
# de la persona que lleno el formulario o ponerlo en el nombre del archivo.

                pdf.output('solicitudes/'+request.POST.get("Nombre")+request.POST.get("Apellido")+'.pdf' )
        
        archivo = open('solicitudes/'+request.POST.get("Nombre")+request.POST.get("Apellido")+'.pdf','rb')
        djangofile = File(archivo)
        solicitud = request.POST.get('Nombre')+request.POST.get('Apellido')+'.pdf'

        #djangofile.name=solicitud
        file_ = {'solicitud': djangofile} 
       
        # if request.method == 'POST':
        #         updated_request = request.POST.copy()
        #         updated_request.update({'solicitud': [file_]})
        request.FILES._mutable = True
        request.FILES.update({'solicitud':  djangofile})

        formulario =  FormContactos(request.POST,request.FILES)       
        
        conn = pypyodbc.win_connect_mdb('static/coopresol.mdb')
        cur = conn.cursor()
        Nombre =str(request.POST.get("Nombre"))
        Apellido = str(request.POST.get("Apellido"))
        Cedula = str(request.POST.get("Cedula"))
        Direccion = str(request.POST.get("Direccion"))
        email = str(request.POST.get("email"))
        Telefono = str(request.POST.get("Telefono"))
        Celular = str(request.POST.get("Celular"))
        Patrocinador = str(request.POST.get("Patrocinador"))
        LugarNacimiento = str(request.POST.get("LugarNacimiento"))
        FechaNacimiento = str(request.POST.get("FechaNacimiento"))
        edadDB = str(request.POST.get("edad"))
        Hijos = str(request.POST.get("Hijos"))
        hijas =str(request.POST.get("hijas"))
        EstadoCivil = str(request.POST.get("EstadoCivil"))
        LugarTrabajo = str(request.POST.get("LugarTrabajo"))
        TelTrabajo = str(request.POST.get("TelTrabajo"))
        DireccionTrabajo = str(request.POST.get("DireccionTrabajo"))
        Estado = str(request.POST.get("Estado"))
        try:
            cur.execute('INSERT INTO PersonFisica (Nombre,Apellido,Cedula,Direccion,email,Telefono,Celular,Patrocinador,LugarNacimiento,FechaNacimiento,edad,Hijos,hijas,EstadoCivil,LugarTrabajo,TelTrabajo,DireccionTrabajo,Estado) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(
                Nombre,
                Apellido,
                Cedula,
                Direccion,
                email,
                Telefono,
                Celular,
                Patrocinador,
                LugarNacimiento,
                FechaNacimiento,
                edadDB,
                Hijos,
                hijas,
                EstadoCivil,
                LugarTrabajo,
                TelTrabajo,
                DireccionTrabajo,
                Estado,
                )
                )  
        except sqlite3.OperationalError as error:
                print("Este registro esta duplicado", error )
               
                #print(formulario.errors.as_data())
             #  print( 'inicio/Asociar.html')
             #  print('inicio/Servicios.html')
        else:
                # poner finaliti aqui
                cur.close() 
                conn.commit() 
                conn.close()
                
        finally:
#guardar el formulario a la base de  datos 
# 
         if formulario.is_valid():
                formulario.save()
                return redirect('inicio') 
           
         else:
             print(request.POST.get('FechaNacimiento'))
             print(formulario.errors.as_data())
        archivo.close()
    context= {
        'contactos':contactos,
        'formulario':formulario,
        'formularioJuridica':formularioJuridica,
        
        
    }
    return render(request,'inicio/Asociar.html',context)


def AsociarseJurudico(request):
          
        pdf = FPDF() # crear variable de librearia fpdf que sirve para crear archivos pdf y en escrbir datos en estos
 

        pdf.add_page()# agrargar pagina
 
        # Establecer el estilo en tamaño de fondo que desees
        pdf.set_font("Arial", size = 15)
        th = pdf.font_size

        if request.method == 'POST':
                pdf.cell(200, 10, txt = "Coopresol",
                        ln = 1, align = 'C')
                pdf.ln(th)
        #aquie termina la declaracion de la primera linea las siguientes lineas estan a continuacion:

                pdf.image( MEDIA_ROOT+"/static/media/avada-charity-logo-retina.png", x = 52, y = None, w = 100, h =20, type = '')

                pdf.cell(200, 10, txt = "Solicitud para asociarse a la Cooperativa",
                        ln = 1, align = 'C')
                pdf.ln(th)
                ##########################################
                pdf.cell(190, 10, txt = "NOMBRE: "+request.POST.get('NombreINS'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'DIRECCION: '+request.POST.get('Direccion'),
                        ln = 1, align = 'l',border=1)  
                ##########################################     
                pdf.cell(190, 10, txt = 'CORRECO ELECTRONICO: '+request.POST.get('email'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'TELEFONO: '+request.POST.get('Telefono'),
                        ln = 1, align = 'l',border=1)
                ##########################################
                pdf.cell(190, 10, txt = 'TELEFONO MOVIL: '+request.POST.get('Celular'),
                        ln = 1, align = 'l',border=1)
                pdf.cell(190, 10, txt = 'SITIO WEB: '+request.POST.get('WebSite'),
                        ln = 1, align = 'l',border=1)
                pdf.cell(190, 10, txt = 'static/media/solicitudes/Solicitud-'+request.POST.get('NombreINS')+'.pdf',
                        ln = 1, align = 'l',border=1)
                pdf.cell(190, 10, txt = 'Firma Organizacion                                      Firma Coopresol',
                        ln = 1, align = 'l')
                pdf.cell(190, 10, txt = '__________________________               ________________________',
                        ln = 1, align = 'l')
# Guardar el archivo con estencoin en pdf en el directorio de static que es directorio base donde django
# trata con archivos estaticos, en este caso uso el mismo request para extraer el nombre y apellido
# de la persona que lleno el formulario o ponerlo en el nombre del archivo.
        
                pdf.output('solicitudes/'+request.POST.get('NombreINS')+'.pdf' )
        
        archivo = open('solicitudes/'+request.POST.get('NombreINS')+'.pdf','rb')
        djangofile = File(archivo)
        solicitud = request.POST.get('NombreINS')+'.pdf'

        #djangofile.name=solicitud
        file_ = {'solicitud': djangofile} 
       
        # if request.method == 'POST':
        #         updated_request = request.POST.copy()
        #         updated_request.update({'solicitud': [file_]})
        request.FILES._mutable = True
        request.FILES.update({'solicitud':  djangofile})
        formulario =  formPerJuridcica(request.POST,request.FILES)       
  
#guardar el formulario a la base de  datos 
# 
        conn = pypyodbc.win_connect_mdb('static/coopresol.mdb')
        cur = conn.cursor()
        Nombre =str(request.POST.get("NombreINS"))
        TipoOrganizacion = str(request.POST.get("TipoOrganizacion"))
        RNC = str(request.POST.get("RNC"))
        Direccion = str(request.POST.get("Direccion"))
        email = str(request.POST.get("email"))
        Telefono = str(request.POST.get("Telefono"))
        Celular = str(request.POST.get("Celular"))
        WebSite = str(request.POST.get("WebSite"))
        PagoRealizado = str(request.POST.get("PagoRealizado"))
        Estado = str(request.POST.get("Estado"))
        # try:
        cur.execute('INSERT INTO PersonaJuridica (Nombre,TipoOrganizacion,RNC,Direccion,email,Telefono,Celular,WebSite,PagoRealizado,Estado) VALUES (?,?,?,?,?,?,?,?,?,?)',(
                Nombre,
                TipoOrganizacion,
                RNC,
                Direccion,
                email,
                Telefono,
                Celular,
                WebSite,
                PagoRealizado,
                Estado,
               
                )
                )  
       #  except sqlite3.OperationalError as error2:
       #          print("Este registro esta duplicado", error2 )
        # else:
        cur.close() 
        conn.commit() 
        conn.close()
       #  finally:
        if formulario.is_valid():
                formulario.save()
                return redirect('inicio') 
        else:
            print('holamundo')
        archivo.close()
    
        return render(request,'inicio/inicio.html',)



def Nosotros(request):
    
    contex={
            #'Salas':salas
    }
    return render(request,'inicio/nosotros.html',contex)


def EquipoPagina(request):

        persona = Equipo.objects.all()
        link = [
        'https://www.youtube.com/embed/7HJ5jd0mMCI',
        'https://www.youtube.com/embed/7HJ5jd0mMCI',
        'https://www.youtube.com/embed/7HJ5jd0mMCI' 
                ]

       
        contex={
           'link':link,
           'persona':persona
        }
        return render(request,'inicio/Equipo.html',contex)


def ProyectosVer(request):
        

        
        formulario = FormProyectos()
        formularioIdeas = FormIdeas()
        link = Link.objects.all()
        categorias = categoria.objects.all()
        formuCategoria = categoria.objects.all()
        proyectos = Proyectos.objects.all()
        
        if request.method =="POST":
                formularioDeIdeas = FormIdeas(request.POST,request.FILES)
                if formularioDeIdeas.is_valid():
                        formularioDeIdeas.save()
                        return redirect('inicio') 
        contex={
        'formulario':formulario,
        'formucategoria':formuCategoria,
        'formularioIdeas':formularioIdeas,
        'proyectos':proyectos,
        'videos': link,
        'categoria':categorias,
        
        }
        return render(request,'inicio/proyectos.html',contex)

def detalles(request,pk):
        proyectos = Proyectos.objects.get(id=pk)
        
        context = {
                'proyectos':proyectos
        }
        return render(request,'inicio/vistaProyecto.html',context)


def Servicios(request):
        
        
        context = {
                
        }
        return render(request,'inicio/Servicios.html',context)

def AulaPagina(request):
       
        videos = Link.objects.all()
        Categoria = categoria.objects.all()
         
        context = {
                'videos':videos,
                'categoria':Categoria
                
        }   
        return render(request,'inicio/Aula.html',context)



def EmailContactar(request):
        correo = request.POST.get('correo')
        formulario = FormCorreo()
#         if request.method == 'POST': 
#                 connection = mail.get_connection()

# # Manually open the connection
#                 connection.open()

# # Construct an email message that uses the connection
#                 email1 = mail.EmailMessage(
#                 request.POST.get('Asunto'),
#                 request.POST.get('mensaje'),
#                 request.POST.get('correo'),
#                 ['kevinnono9619@gmail.com'],
#                 connection=connection,
#                 )
#                 email1.send() # Send the email


# # We need to manually close the connection.
#                 connection.close()
        formulario = FormCorreo(request.POST)
        if formulario.is_valid():
                formulario.save()
                return redirect('Contactanos') 
        context ={
                'formulario':formulario
        
        }
        return render(request,'inicio/Contactanos.html',context)



def busqueda(request):

        
        query = request.GET.get('q') if request.GET.get('q') != None else ''

        equipo= Equipo.objects.filter(
                Q(Nombre__icontains=query) |
                Q(Apellido__icontains=query)|
                Q(Role__icontains=query)|
                Q(HistorialProfesional__icontains=query)
                ).order_by('-id')
        proyecto = Proyectos.objects.filter(
                Q(Titulo__icontains=query) |
                Q(descripcion__icontains=query)
                ).order_by('-id')
        
        videos = Link.objects.filter(
                Q(Titulo__icontains=query) |
                Q(Categoria__Categoria__icontains=query)
                ).order_by('-id')
        categorias = categoria.objects.filter(
                Q(Categoria__icontains=query) |
                Q(Subcategoria__icontains=query)
                ).order_by('-id')

        context={
        'persona':equipo,
        'proyectos':proyecto,
        'videos':videos,
        'categoria':categorias
        }
        return render(request,'inicio/buqueda.html',context)