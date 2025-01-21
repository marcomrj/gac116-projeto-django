from django.db import models
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    nome=models.CharField(max_length=30)
    cpf=models.CharField(max_length=11, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.nome)

class Categoria(models.Model):
    nome=models.CharField(max_length=30)
    def __str__(self) -> str:
        return str(self.nome)
  
class Produto(models.Model):
    nome=models.CharField(max_length=30)
    preco= models.DecimalField(decimal_places=2, max_digits=5)
    descricao=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    imagem = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.nome)

class Pedido(models.Model):
    clienteId = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    mesa=models.IntegerField()
    ativo = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.id)

class PedidoProduto(models.Model):
    class StatusPedidos(models.TextChoices):
        PEDIDO_REALIZADO = '1', _('Pedido Realizado')
        PEDIDO_EM_PREPARO = '2', _('Pedido em Preparo')
        PEDIDO_PRONTO = '3', _('Pedido Pronto')
        PEDIDO_ENTREGUE = '4', _('Pedido Entregue')
    produtoId = models.ForeignKey(Produto, on_delete=models.DO_NOTHING, null=True)
    pedidoId = models.ForeignKey(Pedido, on_delete=models.DO_NOTHING, null=True)
    status = models.CharField(max_length=1,choices=StatusPedidos.choices, default=StatusPedidos.PEDIDO_REALIZADO)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return str(self.id)



