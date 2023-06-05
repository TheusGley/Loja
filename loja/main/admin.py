from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)



class admin_produto (admin.ModelAdmin):
    
    list_display = ('titulo' ,'id', 'categoria','detalhe', 'venda')
    search_fields = ('^titulo',)
    ordering = ('titulo', )



admin.site.register(Produto,admin_produto)
admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Produto_Carrinho)
admin.site.register(Pedido)
