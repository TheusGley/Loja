from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Cor)
admin.site.register(Tamanhos)
admin.site.register(Marcas)


class Produto_admin (admin.ModelAdmin):
    list_display= ('id','titulo','marca','cor','tamanho','status')
    list_editable = ('status',)

admin.site.register(Produto, Produto_admin,)

class Produto_Atributos_Admin (admin.ModelAdmin):
    list_display = ('id','produto','valor', 'cor','tamanho',)

admin.site.register(Produto_atributos,Produto_Atributos_Admin,)