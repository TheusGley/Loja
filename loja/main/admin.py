from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)


admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Carrinho)
admin.site.register(Produto_Carrinho)
admin.site.register(Pedido)



