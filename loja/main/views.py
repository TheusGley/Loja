from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *

# Create your views here.
def produto_destaque (request):
    produto_list = Produto.objects.filter(visualizacao = 10) 
    
    context = { 'produtos' : produto_list }
    
    return render (request , 'index.html', context )

def todos_produtos(request): 
    produto_list = Produto.objects.all()
    categoria_list = Category.objects.all().order_by("-id")
    
    
    context ={ 'produtos': produto_list, 'categorias': categoria_list }
    
    return render(request, 'produto_list.html', context)

def detalhes_produto (request , id):
    
    categoria_list = Category.objects.all().order_by("-id")
    
    produto = get_object_or_404(Produto, id=id)
    titulo_produto = produto.titulo
  
    context ={ 'produto' : produto}
    return render(request, 'detalhe.html', context)
    # return HttpResponse (print (produto))

    

    
    



def produto (request):
    return

