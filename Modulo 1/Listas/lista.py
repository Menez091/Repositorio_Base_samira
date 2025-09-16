lista_de_item=[]
def item_cadastrado():
    item=int(input("digite o livro que irá adicionar: "))
    lista_de_item.append(item)
    print(f" {item} cadastro com sucesso")

def valor():
    valor=float(input("quanto custa o livro:"))
    lista_de_item.append(valor)
    print("livro comprado com sucesso")

def atualizar():
    ...


opção = 0
while opção !=3:
    opção=int(input("digite a opção que deseja: \n 1- adicionar o livro \n 2-ver valor do livro \n 3-atualizar \n 4-remover"))
    if opção == 1:
        item_cadastrado()
    elif opção ==2:
        valor()
    elif opção ==3:
        print("atualizado com sucesso")
    else:
        print("remivido com sucesso")
