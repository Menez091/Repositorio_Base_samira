nome_login=input("digite seu nome de cadastro:")
senha_login=input("digite sua senha de cadastro:")
opcao=7
while opcao !=2:
    nome_cadastrado=input("digite seu nome digitado:")
    senha_cadastrada=input("digite sua senha digitada:")
    
    if nome_login == nome_cadastrado and senha_login == senha_cadastrada:
        print("bem vindo")

    else:
        print("errado tente novamente")
        opcao=int(input("digite 1 para tentar novamente \n 2 para sair"))
