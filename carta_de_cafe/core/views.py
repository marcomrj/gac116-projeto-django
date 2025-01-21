from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Produto, Cliente, Pedido, PedidoProduto
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        mesa = request.POST['mesa']
        

        request.session['mesa'] = mesa
        # Verifica se o cliente já existe pelo CPF
        cliente = Cliente.objects.filter(cpf=cpf).first()

        if cliente:
            # Se o cliente já existe, salva o ID na sessão
            request.session['cliente_id'] = cliente.id
        else:
            # Se o cliente não existe, cria um novo e salva no banco de dados
            cliente = Cliente.objects.create(nome=nome, cpf=cpf)
            request.session['cliente_id'] = cliente.id

        request.session['carrinho'] = {}
        # Redireciona para a página de produtos ou outra página
        return redirect('listar_produtos')

    return render(request, 'produtos/login.html')

def listar_produtos(request):
    produtos = Produto.objects.filter()
    carrinho = request.session.get('carrinho', {})
    if(len(carrinho) < 0):
        carrinho_count = 0
    else:
        carrinho_count = sum(carrinho.values())
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos, 'carrinho_count': carrinho_count})

def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    carrinho = request.session.get('carrinho', {})

    
    if str(produto_id) in carrinho:
        # Se o produto já estiver no carrinho, incrementa a quantidade
        carrinho[str(produto_id)] += 1
    else:
        # Se o produto não estiver no carrinho, adiciona com quantidade 1
        carrinho[str(produto_id)] = 1
    print(carrinho)
    request.session['carrinho'] = carrinho
    
    return redirect('listar_produtos')

def ver_carrinho(request):
    carrinho = request.session.get('carrinho', {})
    produtos = Produto.objects.filter(id__in=carrinho.keys())

    itens_carrinho = []
    for produto in produtos:
        itens_carrinho.append({
            'produto': produto,
            'quantidade': carrinho[str(produto.id)],
            'total': produto.preco * carrinho[str(produto.id)]
        })

    total_carrinho = sum(item['total'] for item in itens_carrinho)

    return render(request, 'produtos/ver_carrinho.html', {
        'itens_carrinho': itens_carrinho,
        'total_carrinho': total_carrinho
    })

def realizar_pedido(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')  # Redireciona para login se o cliente não estiver autenticado


    cliente = Cliente.objects.get(id=cliente_id)
    
    if request.method == 'POST':
        print('teste')
        mesa = request.session['mesa']  # Supondo que o número da mesa seja fornecido

        # Cria o pedido e salva no banco de dados
        pedido = Pedido.objects.create(clienteId=cliente, mesa=mesa, ativo=True)

        # Recupera o carrinho da sessão
        carrinho = request.session.get('carrinho', {})

        # Cria registros em PedidoProduto para cada item no carrinho

        for key, value in carrinho.items():
            print(carrinho)
            for index in range(value):
                produto = Produto.objects.get(id=key)
                PedidoProduto.objects.create(
                    produtoId=produto,
                    pedidoId=pedido,
                    status=PedidoProduto.StatusPedidos.PEDIDO_REALIZADO
                )

        # Limpa o carrinho após realizar o pedido
        request.session['carrinho'] = {}  # Limpa o carrinho após realizar o pedido
        return redirect('pedido_realizado', pedido_id=pedido.id)  # Redireciona para uma página de confirmação

    return render(request, 'produtos/ver_carrinho.html')

def pedido_realizado(request, pedido_id):
    return render(request, 'produtos/pedido_realizado.html', {'pedido_id': pedido_id})

def listar_pedidos_ativos(request):
    cliente_id = request.session.get('cliente_id')
    if not cliente_id:
        return redirect('login')  # Redireciona para login se o cliente não estiver autenticado

    pedidos_ativos = Pedido.objects.filter(clienteId=cliente_id, ativo=True).prefetch_related('pedidoproduto_set')
    
    context = {
        'pedidos_ativos': pedidos_ativos
    }
    return render(request, 'produtos/listar_pedidos_ativos.html', context)

def listar_pedidos_barista(request):
    pedidos_produto = PedidoProduto.objects.select_related('produtoId', 'pedidoId').filter(pedidoId__ativo=True).order_by('created_at')
    
    for pedido_produto in pedidos_produto:
        delta = timezone.now() - pedido_produto.created_at
        pedido_produto.tempo_decorrido = int(delta.total_seconds() // 60)  # Tempo em minutos

    if request.method == 'POST':
        pedido_produto_id = request.POST.get('pedido_produto_id')
        novo_status = request.POST.get('status')

        pedido_produto = PedidoProduto.objects.get(id=pedido_produto_id)
        pedido_produto.status = novo_status
        pedido_produto.save()

        return redirect('listar_pedidos_barista')

    return render(request, 'produtos/listar_pedidos_barista.html', {
        'pedidos_produto': pedidos_produto,
    })

def filtrar_pedidos_por_mesa(request):
    mesa = request.GET.get('mesa')
    pedidos = Pedido.objects.filter(ativo=True)
    
    if mesa:
        pedidos = pedidos.filter(mesa=mesa)
    
    detalhes_pedidos = {}
    for pedido in pedidos:
        detalhes_pedidos[pedido.id] = PedidoProduto.objects.filter(pedidoId=pedido)

    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        pedido = get_object_or_404(Pedido, id=pedido_id)
        pedido.ativo = False
        pedido.save()
        return redirect('filtrar_pedidos_por_mesa')

    return render(request, 'checkout/filtrar_pedidos_por_mesa.html', {
        'pedidos': pedidos,
        'detalhes_pedidos': detalhes_pedidos,
        'mesa': mesa,
    })