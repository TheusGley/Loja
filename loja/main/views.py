from django.shortcuts import render
from .models import *

# Create your views here.
def home (request ):
    produto_list = Produto.objects.all() 
    
    context = { 'produtos' : produto_list }
    
    return render (request , 'index.html', context )


def produto (request):
    return

