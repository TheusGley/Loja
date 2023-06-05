
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', produto_destaque ,  name='destaque'),
    path('produtos', todos_produtos,  name='todos_produtos'),
    path('detalhe/<id>', detalhes_produto,  name='detalhe')
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
