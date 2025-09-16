def cadastrar():
    item=input("digite o livro que irá cadastrar: ")
    print(f" {item} cadastro com sucesso")

def valor():
    valor=float(input("quanto custa o livro:"))
    print("livro comprado com sucesso")

opção = 0
while opção !=3:
    opção=int(input("digite a opção que deseja: \n 1- cadastrar o livro \n 2-valor do livro \n 3- SAIR"))
    if opção == 1:
        cadastrar()
    elif opção ==2:
        valor()
    elif opção ==3:
        print("voce saiu com sucesso")
