from django.db import models

# Create your models here


class Banner (models.Model):
    img = models.CharField(max_length=250)
    alt_txt = models.CharField(max_length=300) 

class Category (models.Model):
    titulo = models.CharField(max_length=180 ) 
    image = models.ImageField( upload_to="cat_img", height_field=None, width_field=None, max_length=None)
    
    def  __str__(self) :
        return self.titulo
    
class Cor (models.Model):
    titulo = models.CharField(max_length=180 ) 
    color_codigo = models.CharField(max_length=100)

    def  __str__(self) :
        return self.titulo 
        
class Tamanhos (models.Model):
    titulo = models.CharField(max_length=100 ) 


    def  __str__(self) :
        return self.titulo 
        
class Marcas (models.Model):
    titulo = models.CharField(max_length=180 ) 
    image = models.ImageField( upload_to="cat_img", height_field=None, width_field=None, max_length=None)


    def  __str__(self) :
        return self.titulo 
    
class Produto (models.Model):
    titulo = models.CharField(max_length=180 ) 
    image = models.ImageField( upload_to="produto_img", height_field=None, width_field=None, max_length=None)

    nome = models.CharField(max_length=200 )
    detalhe =models.TextField() 
    especificao =models.TextField() 
    valor = models.PositiveBigIntegerField()
    marca = models.ForeignKey(Marcas , on_delete= models.CASCADE)
    categoria = models.ForeignKey(Category , on_delete= models.CASCADE)
    cor  = models.ForeignKey(Cor , on_delete= models.CASCADE)
    tamanho = models.ForeignKey(Tamanhos , on_delete= models.CASCADE)
    status = models.BooleanField(default=True)
    


    def  __str__(self) :
        return self.titulo 
    
    
class Produto_atributos(models.Model):
    
    produto = models.ForeignKey(Produto,  on_delete=models.CASCADE)  
    cor = models.ForeignKey(Cor,  on_delete=models.CASCADE)
    tamanho = models.ForeignKey(Tamanhos, on_delete=models.CASCADE)
    valor = models.PositiveIntegerField()
    
    def __str__ (self):
        return self.produto.titulo
    
    