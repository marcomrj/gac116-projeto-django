from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Produto, Categoria

@receiver(post_migrate)
def criar_produtos_iniciais(sender, **kwargs):
    if sender.name == "core":
        categoria_padrao, _ = Categoria.objects.get_or_create(nome="Outros")

        produtos = [
            {
                "nome": "Espresso",
                "preco": 8.00,
                "descricao": "Café puro e forte.",
                "categoria": categoria_padrao,
                "imagem": "espresso.png",
            },
            {
                "nome": "Cappuccino",
                "preco": 12.00,
                "descricao": "Espuma, café e leite.",
                "categoria": categoria_padrao,
                "imagem": "cappuccino.png",
            },
            {
                "nome": "Latte",
                "preco": 10.00,
                "descricao": "Café suave com leite.",
                "categoria": categoria_padrao,
                "imagem": "latte.png",
            },
            {
                "nome": "Macchiato",
                "preco": 9.00,
                "descricao": "Café com toque de espuma.",
                "categoria": categoria_padrao,
                "imagem": "macchiato.png",
            },
            {
                "nome": "Mocha",
                "preco": 14.00,
                "descricao": "Café com chocolate.",
                "categoria": categoria_padrao,
                "imagem": "mocha.png",
            },
        ]

        for produto in produtos:
            Produto.objects.get_or_create(nome=produto["nome"], defaults=produto)
