"""10. Simulador de Loja Virtual no Terminal
O projeto mais completo: exibe produtos, permite adicionar ao carrinho e finalizar a compra. Tudo
no terminal, simulando um e-commerce. Trabalha organização de dados, lógica condicional e
menus encadeados."""
#Importações essenciais para o front-end e o back-end com banco de dados
import pyfiglet
import emoji
from rich.console import Console
from tabulate import tabulate
from colorama import init, Fore, Style
init(autoreset=True)
import mysql.connector

#Parte essencial para conectar meu código com o Banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Miguel11!",
    database="lojavirtual"
)


#Exibe um titulo bonito
print(pyfiglet.figlet_format("Lojinha do Ze"))


#Parte que cria a ferramenta que o Python usa para conversar com o banco de dados. Sem isso, nada funciona.
cursor = conexao.cursor()  #conexao.cursor().execute

#Seleciona todos os dados dos produtos e exibe de maneira visualmente bonita
def selecionar_all_produtos():
  cursor.execute("SELECT * FROM produtos")
  resultados = cursor.fetchall()
  for linha in resultados:
     headers = [
     f"{Fore.GREEN}ID{Style.RESET_ALL}",
     f"{Fore.MAGENTA}Nome{Style.RESET_ALL}",
     f"{Fore.CYAN}Preço (R$){Style.RESET_ALL}"
      ]
     print(tabulate([linha], headers=headers, tablefmt="fancy_grid"))

selecionar_all_produtos()

produtosEscolhidos = []

#Essa parte do codigo, pega todos os ids do banco, e coloca numa lista na variavel idsDisponiveis.
#E verifica no banco, se existir o produto, ele é adicionado ao carrinnho.
cursor.execute("SELECT id_produto FROM produtos")
idsDisponiveis = [linha[0] for linha in cursor.fetchall()]  
def obter_id_produto():
 while True:
    entrada = input("\nEscolha o produto de acordo com ID ou feche clicando ENTER: ")

    if entrada == "":
        print(Fore.MAGENTA + "Encerrando...")
        return ""

    if not entrada.isdigit():
        print(Fore.RED + "Erro: Digite apenas números, letras não são permitidas")
        continue

    produto = int(entrada)

    if produto not in range(1, 5):  # vai de 1 a 3
        print(emoji.emojize(Fore.RED + ":warning:  ATENÇÃO :warning:  --> ESCREVA O ID DE 1 A 4", language='alias'))
        continue

    print(Fore.GREEN + f"ID {produto} aceito.")
    return produto

produto = obter_id_produto()

if produto in idsDisponiveis:
   print(Fore.MAGENTA + "------------> Produto Adicionado ao carrinho <------------\n")
   
   #Essa parte é do cadastro, funciona da mesma maneira, ela pega os nomes do banco e armazena.
   #E no códgio o usuario verifica o nome dele, se o nome dele não estiver cadastrado, o cod pula para a parte do cadastro e manda pro banco os dados
   cursor.execute("SELECT nome from clientes")
   nomesCadastrados = [linha[0].strip().lower() for linha in cursor.fetchall()]
   while True:
       confirmacaoCadastro = input(Fore.CYAN + "VOCÊ TEM CADASTRO NA LOJA DO ZE?(s/n): ").strip().lower()

       if confirmacaoCadastro.isdigit():
           print(Fore.YELLOW + "Erro: Confirme com (s) para SIM e (n) para não, não use números")
           continue
       if confirmacaoCadastro in ["sim", "s", "n", "não"]:
         break
       else:
          continue
   
      

   if confirmacaoCadastro == "s" or confirmacaoCadastro == "sim":
       while True:
           confirmacaoNome = input("DIGITE SEU NOME CADASTRADO: ").strip().lower()
           if all(parte.isalpha() for parte in confirmacaoNome.split()):
               break
           else:
              print("Seu nome deve ser escrito por letras, não números. Seu animal")
       if confirmacaoNome in nomesCadastrados:
           print(emoji.emojize(Fore.GREEN + "\nVOCÊ ESTÁ CADASTRADO :smiley:, BOA COMPRA\n", language='alias')) #Com Adição de Emoji
           #Parte do código que simula a compra, não tem banco para isso, pois esses dados não podem ser registrados
           print(Fore.YELLOW + "INICIANDO PAGAMENTO...")
           numerodocartao = int(input(Fore.LIGHTBLUE_EX + "DIGITE O NÚMERO DO SEU CARTÃO: "))
           dataExpiracao = int(input(Fore.LIGHTBLUE_EX + "DIGITE A DATA DE EXPIRAÇÃO DO CARTÃO: "))
           codSeguranca = int(input(Fore.LIGHTBLUE_EX + "DIGITE O CÓDIGO DE SEGURANÇA DO CARTÃO: "))
   elif confirmacaoCadastro == "n" or confirmacaoCadastro == "não":
        print(emoji.emojize(Fore.YELLOW + "VOCÊ AINDA NÃO TEM CADASTRO :cry:, CADASTRE-SE ABAIXO :smiley: ", language='alias'))
        while True:
           nomeDoCliente = input(Fore.LIGHTGREEN_EX + "DIGITE SEU NOME: ")
           if all(parte.isalpha() for parte in nomeDoCliente.split()):
               break
           print(Fore.RED + "Erro: Digite letras, sem números ou símbolos")
        while True:
          rua = input(Fore.LIGHTGREEN_EX + "DIGITE SUA RUA: ")
          if all(parte.isalpha() for parte in rua.split()):
              break
          print(Fore.RED + "Erro: Digite letras, sem números ou símbolos") 
        while True:
           numeroCasa = input(Fore.LIGHTGREEN_EX + "DIGITE O NÚMERO DA CASA: ")
           if numeroCasa.isdigit():
               break
           print(Fore.RED + "Erro: Digite números, sem letras ou símbolos") 
        
           
        while True:
          telefone = input(Fore.LIGHTGREEN_EX + "DIGITE SEU TELEFONE: ")
          if telefone.isdigit():
              break
          print(Fore.RED + "Erro: Digite números, sem letras ou símbolos") 
        cursor.execute("INSERT INTO clientes(nome, rua, numerodacasa, telefone) VALUES(%s, %s, %s, %s)", (nomeDoCliente, rua, numeroCasa, telefone,))
        conexao.commit()
        print(Fore.GREEN + "------> CADASTRO FEITO <------")
        #Parte do código que simula a compra, não tem banco para isso, pois esses dados não podem ser registrados
        print(Fore.YELLOW + "INICIANDO PAGAMENTO...")
        numerodocartao = int(input(Fore.LIGHTBLUE_EX + "DIGITE O NÚMERO DO SEU CARTÃO: "))
        dataExpiracao = int(input(Fore.LIGHTBLUE_EX + "DIGITE A DATA DE EXPIRAÇÃO DO CARTÃO: "))
        codSeguranca = int(input(Fore.LIGHTBLUE_EX + "DIGITE O CÓDIGO DE SEGURANÇA DO CARTÃO: "))

   

  #Parte final do código, se o usuario realmente querer finaliar a compra, o registro de venda é mandado para
  #a tabela vendas, caso contrario cancela a compra e nada é de fato registrado no banco
   continuar = input(f"\n\n{Style.RESET_ALL}Você está quase lá, deseja finalizar a compra(s/n)?{Style.RESET_ALL} ").strip().lower()
   if continuar == "s" or continuar == "sim" or continuar == "yes":
       cursor.execute('INSERT INTO vendas(id_produto) values(%s)', (produto,))
       conexao.commit()
       print(Fore.GREEN + "------------> COMPRA REALIZADA COM SUCESSO <------------")
   else:
       while True:
         selecionar_all_produtos()
         cursor.execute("SELECT id_produto FROM produtos")
         idsDisponiveis = [linha[0] for linha in cursor.fetchall()]  
         produto2 = obter_id_produto()
         
         if produto2 in idsDisponiveis:
            print(Fore.MAGENTA + "------------> Produto Adicionado ao carrinho <------------")
            produtosEscolhidos.append(produto2)
            finalizar = input(Fore.BLUE  + f"Deseja finalizar a compra(s/n)? {Style.RESET_ALL}").strip().lower()
            if finalizar == "s" or finalizar == "sim":
                cursor.execute('INSERT INTO vendas(id_produto) values(%s)', (produto,))
                cursor.executemany('INSERT INTO vendas(id_produto) VALUES (%s)', [(id,) for id in produtosEscolhidos])
                conexao.commit()
                print(Fore.GREEN + "------------> COMPRA REALIZADA COM SUCESSO <------------")
                break
            else:
                continue
         elif produto2 == "":
            print(Fore.YELLOW+"Nenhum produto extra adicionado")
            cursor.execute('INSERT INTO vendas(id_produto) values(%s)', (produto,))
            cursor.executemany('INSERT INTO vendas(id_produto) VALUES (%s)', [(id,) for id in produtosEscolhidos])
            conexao.commit()
            break

         else:
             ("PRODUTO NÃO EXISTE")


       
       
            
    


    

