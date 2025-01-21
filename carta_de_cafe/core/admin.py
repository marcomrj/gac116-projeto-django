from django.contrib import admin
from .models import Produto, Pedido, Cliente, Categoria, PedidoProduto
from django.utils.html import format_html

admin.site.register(Categoria)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('image_tag','nome', 'preco', 'nome_categoria')
    search_fields = ('nome',)
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.imagem.url))
    image_tag.admin_order_field  = 'imagem'
    image_tag.short_description = 'Imagem Produto' 
    def nome_categoria(self, obj):
        return obj.categoria.nome
    
    nome_categoria.admin_order_field  = 'nome categoria'
    nome_categoria.short_description = 'Nome Categoria' 
    


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id',  'mesa', 'ativo')
    list_filter= ('ativo',)
    
@admin.register(PedidoProduto)
class PedidoProdutoAdmin(admin.ModelAdmin):
    list_display = ('numero_pedido',  'nome_produto', 'numero_mesa', 'status')
    def numero_pedido(self, obj):
        return obj.pedidoId.id
    def nome_produto(self, obj):
        return obj.produtoId.nome
    def numero_mesa(self, obj):
        return obj.pedidoId.mesa
    numero_pedido.admin_order_field  = 'numero pedido'
    numero_pedido.short_description = 'numero Pedido' 
    nome_produto.admin_order_field  = 'nome produto'
    nome_produto.short_description = 'nome Produto' 
    
