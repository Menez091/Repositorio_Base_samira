opcao=10
while opcao!=4:
    opcao=int(input("digite q deseja fazer: \n1-fazer o pix\n2-extrato\n3-depositar\n4-sair"))
    if opcao==1:
        valor= input("digite o valor que deseja mandar:")
        quem=input("digite para quem eu vou mandar:")
        print("transferencia realizada:")
    elif opcao==2:
      saldo=input("digite o valor de saldo:")
    elif opcao==3:
        deposito=input("digite o valor depositado:")
        print("valor enviado")
else:
    sair=input(" digite o valor que ira sair da conta:")
    print("o dinheiro foi retirado")
