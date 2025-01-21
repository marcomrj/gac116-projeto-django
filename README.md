# Carta de Café

Este é um projeto Django chamado **Carta de Café**, desenvolvido para gerenciar e exibir um cardápio virtual de produtos como diferentes tipos de cafés e outras bebidas. O objetivo é oferecer uma interface para administração e visualização de produtos de maneira simples e eficiente.

## Funcionalidades
- Listagem de produtos no cardápio.
- Gerenciamento de produtos e categorias via painel administrativo.
- Suporte à adição de imagens e descrições detalhadas para cada produto.
- Registra automaticamente produtos iniciais no banco de dados após a migração (produtos padrão).

## Como Rodar o Projeto
Siga os passos abaixo para rodar o projeto sem criar um ambiente virtual:

### 1. Requisitos Pré-Instalados
Certifique-se de que você tem as seguintes dependências instaladas no sistema:
- Python 3.10 ou superior
- Django (instale com `pip install django` se ainda não estiver instalado)

### 2. Clone o Repositório
Faça o clone do repositório para o seu ambiente local:
```bash
git clone https://github.com/seu_usuario/carta_de_cafe.git
cd carta_de_cafe
```

### 3. Configure o Banco de Dados
Inicialize as migrações para configurar o banco de dados:
```bash
python manage.py migrate
```

### 4. Inicialize o Servidor de Desenvolvimento
Inicie o servidor de desenvolvimento para testar a aplicação:
```bash
python manage.py runserver
```
Acesse o projeto no navegador em [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 5. (Opcional) Acesse o Painel Administrativo
Se desejar acessar o painel administrativo do Django, crie um superusuário:
```bash
python manage.py createsuperuser
```
Preencha os dados solicitados (usuário, e-mail e senha) e acesse [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).

## Estrutura do Projeto
- **core/**: Contém os modelos, views e lógica principal da aplicação.
- **templates/**: Arquivos HTML para renderização das páginas.
- **static/**: Arquivos estáticos como CSS, JavaScript e imagens.
- **db.sqlite3**: Banco de dados SQLite usado para desenvolvimento.

## Problemas Comuns
- **Erro: That port is already in use**: Isso ocorre quando o porto padrão (8000) está em uso. Resolva rodando o servidor em outro porto:
  ```bash
  python manage.py runserver 8080
  ```

- **Tabelas já existem**: Caso encontre erros relacionados a tabelas existentes, remova o arquivo `db.sqlite3` e as migrações antigas em `core/migrations` e refaça as migrações.

## Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

