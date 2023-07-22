from django.contrib import admin

from aplicacion_2.models import registroUsuarios, Proveedores

class UsuariosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'direccion', 'email', 'ciudad')

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('nombre_empresa', 'email_empresa', 'fono_empresa', 'rubro_empresa')


admin.site.register(registroUsuarios, UsuariosAdmin)
admin.site.register(Proveedores)