

# README - Lojinha do Ze - Simulador de Loja Virtual no Terminal

## Sobre o Projeto

Este projeto é um simulador de loja virtual que roda no terminal (Prompt de Comando). Ele permite:

* Visualizar os produtos disponíveis
* Adicionar produtos ao carrinho
* Fazer cadastro de clientes (se não estiver cadastrado)
* Simular pagamento (sem de fato pagar nada, apenas para deixar o código completo)
* Finalizar a compra

O sistema conecta a um banco de dados MySQL para armazenar produtos, clientes e registrar as vendas.

---

## Como o código funciona

1. Conecta ao banco MySQL local usando usuário, senha e nome do banco configurados no código.

2. Exibe todos os produtos disponíveis com IDs, nomes e preços.

3. Solicita que o usuário escolha o produto digitando o ID.

4. Valida se o ID é válido e existe na lista de produtos.

5. Pergunta se o cliente já tem cadastro na loja:

   * Se sim: pede o nome cadastrado e verifica no banco.
   * Se não: solicita dados para cadastro (nome, endereço, telefone) e grava no banco.

6. Simula a etapa de pagamento (pede dados do cartão, mas não grava no banco).

7. Pergunta se deseja finalizar a compra ou adicionar mais produtos.

8. Registra as vendas no banco de dados.

---

## Estrutura do banco de dados (simplificada)

Você precisa criar um banco MySQL chamado **lojavirtual** com essas tabelas:

* **produtos**
  → id\_produto (inteiro, chave primária, auto-incremento)
  → nome (texto)
  → preco (decimal)

* **clientes**
  → id\_cliente (inteiro, chave primária, auto-incremento)
  → nome (texto)
  → rua (texto)
  → numerodacasa (texto)
  → telefone (texto)

* **vendas**
  → id\_venda (inteiro, chave primária, auto-incremento)
  → id\_produto (inteiro, chave estrangeira referenciando produtos)

---

## Como criar e configurar o banco no DBeaver



1. Instale o DBeaver:
   → Acesse [https://dbeaver.io/download/](https://dbeaver.io/download/)
   → Baixe e instale a versão Community

2. Crie uma conexão com o MySQL:
   → Clique em “Nova Conexão”
   → Escolha “MySQL”
   → Host: localhost
   → Usuário: root
   → Senha: (sua senha do MySQL)
   → Teste e finalize

3. Crie o banco e as tabelas:
   → Abra um editor SQL
   → Execute este comando para criar o banco:

   
   CREATE DATABASE lojavirtual;
   USE lojavirtual;
   

4. Crie as tabelas (copie e execute):

   
   CREATE TABLE produtos (
     id_produto INT PRIMARY KEY AUTO_INCREMENT,
     nome VARCHAR(100),
     preco DECIMAL(10,2)
   );

   CREATE TABLE clientes (
     id_cliente INT PRIMARY KEY AUTO_INCREMENT,
     nome VARCHAR(100),
     rua VARCHAR(100),
     numerodacasa VARCHAR(10),
     telefone VARCHAR(15)
   );

   CREATE TABLE vendas (
     id_venda INT PRIMARY KEY AUTO_INCREMENT,
     id_produto INT,
     FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
   );
   

5. Insira alguns produtos para testar:

   
   INSERT INTO produtos (nome, preco) VALUES
   ('Camiseta', 39.90),
   ('Calça Jeans', 89.90),
   ('Tênis Esportivo', 149.90),
   ('Boné', 25.00);
   



---

## Instalando as bibliotecas Python necessárias

### Usando o arquivo `requirements.txt`

Para facilitar a instalação das bibliotecas, criamos um arquivo chamado **requirements.txt** com a lista de dependências usadas no projeto.

### Passos para usar o `requirements.txt`:

1. Salve o arquivo **requirements.txt** na mesma pasta do seu projeto. Ele deve conter:

   
   pyfiglet
   emoji
   rich
   tabulate
   colorama
   mysql-connector-python
   

2. Abra o terminal do sistema **ou** o terminal integrado do VS Code (menu Terminal > Novo Terminal).

3. Execute o comando para instalar todas as bibliotecas de uma vez:

   
   pip install -r requirements.txt


---

### Dicas importantes:

* No VS Code, use o terminal integrado para garantir que as bibliotecas sejam instaladas no ambiente correto.

* Se tiver mais de uma versão do Python, pode usar:


  python -m pip install -r requirements.txt


  ou


  python3 -m pip install -r requirements.txt


* Para verificar qual interpretador Python o VS Code está usando, clique no canto inferior esquerdo da janela do VS Code e selecione o ambiente correto.

---

## Como rodar o código

* Certifique-se que as bibliotecas estão instaladas (via `requirements.txt` ou comando `pip install`).

* Ajuste no código os dados da conexão com o banco (`host`, `user`, `password`, `database`) se necessário.

* Execute o script Python no terminal:

 
  python nome_do_arquivo.py


* Siga as instruções na tela para escolher produtos, fazer cadastro e finalizar a compra.



---



