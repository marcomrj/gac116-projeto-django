# Carta de Café

## Descrição

O **Carta de Café** é um sistema de gerenciamento de pedidos para cafeterias, desenvolvido com **Django**. O projeto permite que clientes realizem pedidos, adicionem produtos ao carrinho e acompanhem o status do pedido. Os baristas podem gerenciar os pedidos e atualizar o status de cada um.

---

## Tecnologias Utilizadas

- **Django 5.0.7** (Framework Web)
- **SQLite** (Banco de Dados Padrão)
- **HTML, CSS e JavaScript** (Templates Django)

---

## Funcionalidades

- **Clientes:**
  - Login utilizando CPF e nome.
  - Visualização de produtos disponíveis.
  - Adição de produtos ao carrinho.
  - Realização de pedidos.
  - Acompanhamento dos pedidos ativos.
  
- **Barista/Admin:**
  - Gestão de produtos e categorias.
  - Gerenciamento de pedidos e atualização de status.
  - Controle de pedidos por mesa.

---

## Como Rodar o Projeto

### 1. Clone o Repositório
```bash
    git clone https://github.com/seu-usuario/carta-de-cafe.git
    cd carta-de-cafe
```

### 2. Crie um Ambiente Virtual e Ative
```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
```

### 3. Instale as Dependências
```bash
    pip install -r requirements.txt
```

### 4. Configure o Banco de Dados
```bash
    python manage.py migrate
```

### 5. Popule o Banco com Produtos Padrão
```bash
    python manage.py runserver
```

### 6. Crie um Superusuário (Opcional, para acesso ao Django Admin)
```bash
    python manage.py createsuperuser
```

### 7. Inicie o Servidor
```bash
    python manage.py runserver
```

Acesse: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Estrutura do Projeto

```
carta-de-cafe/
│── core/                # Aplicação principal
│   ├── migrations/      # Migrations do banco de dados
│   ├── static/          # Arquivos estáticos (CSS, JS, imagens)
│   ├── templates/       # Templates HTML
│   ├── admin.py         # Configuração do Django Admin
│   ├── apps.py          # Configuração do app Django
│   ├── models.py        # Modelos do banco de dados
│   ├── views.py         # Lógica das páginas
│   ├── urls.py          # Rotas do app
│   ├── signals.py       # Geração automática de produtos iniciais
│── admin_django/        # Configuração principal do projeto
│── db.sqlite3           # Banco de dados SQLite
│── manage.py            # Comando de gerenciamento Django
│── requirements.txt     # Dependências do projeto
│── README.md            # Documentação
```

---

## Melhorias Futuras

- Implementar autenticação padrão do Django.
- Migrar o banco de dados para PostgreSQL.
- Criar um painel mais interativo para os baristas.

---

## Licença

Este projeto é de código aberto sob a licença MIT.

