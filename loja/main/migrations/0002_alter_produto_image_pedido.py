# Generated by Django 4.1.7 on 2023-06-02 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='image',
            field=models.ImageField(upload_to='static/media/produto_img'),
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordenador_por', models.CharField(max_length=200)),
                ('endereco_envio', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('subtotal', models.PositiveIntegerField()),
                ('desconto', models.PositiveIntegerField()),
                ('total', models.PositiveIntegerField()),
                ('pedido_status', models.CharField(choices=[('Pedido Processando', 'Pedido Processando'), ('Pedido Completado', 'Pedido Completado'), ('Pedido Recebido', 'Pedido Recebido'), ('Pedido Cancelando', 'Pedido Cancelando'), ('Pedido a Caminho', 'Pedido a Caminho')], max_length=300)),
                ('criado_em', models.DateField(auto_now_add=True)),
                ('carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carrinho')),
            ],
        ),
    ]
