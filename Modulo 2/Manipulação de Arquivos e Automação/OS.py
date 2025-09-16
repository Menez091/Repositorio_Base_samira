import os
# print("Diretório atual:")
# print(os.getcwd())

# os.mkdir("projetos")
# print("Pasta criada!")

# txt=open("Projetos/matematica.txt", "w").close(),open("Projetos/portugues.txt", "w").close(),open("Projetos/ciencias.txt", "w").close()


# arquivos = os.listdir("projetos")
# for item in arquivos:
#     print(item)

# os.rename("projetos/ciencias.txt", "projetos/historia.txt")

if os.path.exists("matematica.txt"):
    os.remove("matematica.txt")
    print("Arquivo apagado")
else:
    print("Arquivo não encontrado")
