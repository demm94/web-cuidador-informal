from django.contrib import admin
#from .models import Seccion, Topico, Subtopico
from.models import Topico, Subtopico, Tema, DetalleTema

# Register your models here.

class TopicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado_por', 'fecha_creacion')
    fieldsets = (
        (None, { 'fields': ['nombre', 'imagen', 'url_infografia'] } ),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creado_por', None) is None:
            obj.creado_por = request.user
        obj.save()

class SubTopicoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'topico', 'creado_por', 'fecha_creacion')
    fieldsets = (
        (None, { 'fields': ('nombre', 'topico', 'imagen') } ),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creado_por', None) is None:
            obj.creado_por = request.user
        obj.save()

class TemaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'subtopico', 'topico', 'creado_por', 'fecha_creacion')
    fieldsets = (
        (None, { 'fields': ('nombre', 'subtopico', 'topico', 'imagen') } ),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creado_por', None) is None:
            obj.creado_por = request.user
        obj.save()

class DetalleTemaAdmin(admin.ModelAdmin):
    list_display = ('id','tema','subtopico', 'topico', 'creado_por', 'fecha_creacion')
    fieldsets = (
        (None, { 'fields': ('descripcion', 'tema', 'subtopico', 'topico') } ),
    )

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'creado_por', None) is None:
            obj.creado_por = request.user
        obj.save()

#admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Topico, TopicoAdmin)
admin.site.register(Subtopico, SubTopicoAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(DetalleTema, DetalleTemaAdmin)