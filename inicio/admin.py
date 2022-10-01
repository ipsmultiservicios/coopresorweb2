from django.contrib import admin

# Register your models here.

from .models import Contactos,Proyectos,Equipo,Link,categoria,Correo,SociosJuridicos,Ideas,User
from administracion.models import User

admin.site.register(Contactos)
admin.site.register(Proyectos)
admin.site.register(Equipo)
admin.site.register(Link)
admin.site.register(categoria)
admin.site.register(Correo)
admin.site.register(SociosJuridicos)
admin.site.register(Ideas)
admin.site.register(User)
