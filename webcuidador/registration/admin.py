from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class MyUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'is_medico', 'is_cuidador', 'is_gestionador', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('is_medico', 'is_cuidador', 'is_gestionador')}),
    )
admin.site.register(User, MyUserAdmin)