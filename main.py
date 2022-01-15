import requests

def escolha(escolha="s"):
  if escolha == "s":
    return True
  elif escolha == "n":
    return False
  else:
    print("Caracter inválido")

url_gov = []
url_com = []
while(True):
  print("="*45)
  print("(1) Adicionar sites comuns")
  print("(2) Adicionar Sites governamentais")
  print("(3) Listar sites com .gov")
  print("(4) Listar sites comuns")
  print("(5) Excluir site comum")
  print("(6) Excluir site gov")
  print("(7) Request ")
  print('(x) Sair do programa') 
   
  print("="*45)
  try:
    opcoes = ["1", "2", "3", "4","5","6","7","x" ]
    opcao = input('opcao:')
    opcao.lower()
    assert opcao in opcoes

    if opcao == "1":
      while (escolha()):
        site = input("Digite o nome do site ").lower().strip()
        correct_site = "http://"+ site + ".com"
        url_com.append(correct_site)
        answer = input("Deseja continuar adicionando sites? s/n  ").lower()
        if escolha(answer) == False : break

    elif opcao == "2":
      while (escolha()):
        site = input("Digite o nome do site governamental: ").lower().strip()
        correct_site = "http://"+ site + ".gov.br"
        url_gov.append(correct_site)
        answer = input("Deseja continuar adicionando sites? s/n ").lower()
        if escolha(answer) == False : break
    
    elif opcao == "3":
      if len(url_gov)!= 0:
        for i,j in enumerate(url_gov):
          print(i,j)
      else:
        print("Está lista Está vazia")
    
    elif opcao == "4":
      if len(url_com)!=0:
        for i,j in enumerate(url_com):
          print(i,j)
      else:
        print("Está Lista está vazia")
    
    elif opcao == "5":
      try:
        if len(url_com)!= 0:
          for i,j in enumerate(url_com):
            print(i,j)
          excluir = int(input("Escolha o número referente ao site para excluílo: "))
          del(url_com[excluir])
        else:
          print("A lista está vazia, por isso não é possível excluir")
      except IndexError as ie:
        print("O número não está disponível")
      except ValueError as ve:
        print("Digite um número inteiro")
    elif opcao == "6":
      try:
        if len(url_gov)!= 0:
          for i,j in enumerate(url_gov):
            print(i,j)
          excluir = int(input("Escolha o número referente ao site para excluílo: "))
          del(url_gov[excluir])
        else:
          print("A lista está vazia, por isso não é possível excluir")
      except IndexError as ie:
        print("O número não está disponível")
      except ValueError as ve:
        print("Digite um número inteiro")
    elif opcao == "7":
      
      try:
        print("(g) - para sites do governo")
        print("(c) - para sites comuns")
        decisoes = ["g", "c"]
        decisao = input("escolha: ").lower()
        assert decisao in decisoes
        if decisao == "g":
          if len(url_gov) == 0:
            print("A lista de site está vazia")
          else:
            for i in range(len(url_gov)):
              request_result = requests.get(url_gov[i])
              http_result = request_result.status_code
              match http_result :
                case 400:
                    print(f"Bad request -> {url_gov[i]}")
                case 404:
                    print(f"Not found -> {url_gov[i]}")
                case 418:
                    print(f"I'm a teapot -> {url_gov[i]}")
                case _:
                    print("Something's wrong with the internet")
        
        elif decisao == "c":
          if len(url_com) == 0:
            print("A lista está vazia")
          else:
            for i in range(len(url_com)):
              request_result = requests.get(url_com[i])
              http_result = request_result.status_code
              match http_result :
                case 200:
                    print(f"Site está on - > {url_com[i]}")
                case 400:
                    print(f"Bad request -> {url_com[i]}")
                case 404:
                    print(f"Not found -> {url_com[i]}")
                case 418:
                    print(f"I'm a teapot -> {url_com[i]}")
                case _:
                    print("Something's wrong with the internet")
        

      except AssertionError:
        print("Escolha não está disponível")


    
  except AssertionError:
    print("A opção digitada não está disponível")