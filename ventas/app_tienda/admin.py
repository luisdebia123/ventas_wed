from django.contrib import admin
from .models import Categoria_Prod, Productos
# Register your models here.


class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields =('created','updated')


admin.site.register(Categoria_Prod)
admin.site.register(Productos)