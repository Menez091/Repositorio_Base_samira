nome=str(input("digite seu nome?"))
peso=float(input("qual é o seu peso?"))
altura=float(input("qual a sua altura?"))

IMC=(peso/altura * altura)

if peso>=30:
    print("pescisa se cuidar mais")
elif  peso>=60:
    print("tudo ok")
elif peso>=80:
    print("precisa fazer exercicios e ter uma alimentação regulada")
else: peso>=100
print("precisa ir urgentemente para o medico")
