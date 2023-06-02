from django.db import models
from django.contrib.auth.models import User


# Create your models here


PEDIDO_STATUS = {
    ("Pedido Recebido" , "Pedido Recebido"),
    ("Pedido Processando" , "Pedido Processando"),
    ("Pedido a Caminho" , "Pedido a Caminho"),
    ("Pedido Completado" , "Pedido Completado"),
    ("Pedido Cancelando" , "Pedido Cancelando"),

}   

class Category (models.Model):
    titulo = models.CharField(max_length=180 ) 
    slug = models.SlugField(unique=True)
    image = models.ImageField( upload_to="cat_img", height_field=None, width_field=None, max_length=None)
    
    def  __str__(self) :
        return self.titulo
    

class Produto (models.Model):
    titulo = models.CharField(max_length=180 ) 
    image = models.ImageField( upload_to="produto_img", height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(unique=True)
    categoria =  models.ForeignKey(Category , on_delete=models.CASCADE)
    preco_mercado = models.PositiveIntegerField()
    venda = models.PositiveIntegerField()
    especificao =models.TextField() 
    detalhe =models.TextField() 
    garantia = models.CharField(max_length=300 , null=True, blank=True)
    return_devolucao = models.CharField(max_length=300 , null=True, blank=True)
    visualizacao = models.PositiveIntegerField(default=0) 
   


    def  __str__(self) :
        return self.titulo 
    
    
class Cliente (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo =  models.CharField(max_length=300, null=True) 
    endereco  =  models.CharField(max_length=300 ,null=True) 
    data_cadastro  = models.DateTimeField(auto_now_add = True)
    
    def  __str__(self) :
        return self.nome_completo
    
    
    
class Carrinho (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank = True)
    total = models.PositiveIntegerField(default=0)
    data_criado = models.DateField(auto_now_add=True)
    
    def  __str__(self) :
        
        return Carrinho  + str(self.id)

class Produto_Carrinho (models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    avaliacao =  models.PositiveIntegerField()
    quantidade = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()
    
    def  __str__(self) :
        
        return "Carrinho: " + str(self.Carrinho.id)+"Produto:"+ str(self.id)
    
class Pedido (models.Model):
    carro = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    ordenador_por = models.CharField(max_length=200)
    
    endereco_envio = models.CharField( max_length=200)
    telefone  = models.CharField( max_length=10)
    email = models.EmailField (max_length=254)
    subtotal = models.PositiveIntegerField()
    desconto = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    pedido_status =  models.CharField( max_length=300 ,  choices=PEDIDO_STATUS)
    criado_em =  models.DateField( auto_now_add=True)
     