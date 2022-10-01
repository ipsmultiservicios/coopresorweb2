from django.conf import settings
from  django.urls import URLPattern, path
from . import views
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import *

urlpatterns=[
    path('',views.Inicio,name="inicio"),
    path('Asociarse',views.Asociate,name="Asociarse"),
    path('AsociarseJuridica',views.AsociarseJurudico,name="Juridica"),
    path('Nosotros',views.Nosotros,name="Nosotros"),
    path('Equipo',views.EquipoPagina,name="Equipo"),
    path('Proyectos',views.ProyectosVer,name="Proyectos"),
    path('proyectos/Detalles<str:pk>',views.detalles,name="Detalles"),
    path('Servicios',views.Servicios,name="Servicios"),
    path('Aprende',views.AulaPagina,name="Aprende"),
    path('Contactanos',views.EmailContactar,name="Contactanos"),
    path('busqueda',views.busqueda,name="busqueda"),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)