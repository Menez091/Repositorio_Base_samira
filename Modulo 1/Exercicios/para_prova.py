nome=str(input("digite seu nome?"))
peso=float(input("qual é o seu peso?"))
altura=float(input("qual a sua altura?"))

IMC=peso/(altura * altura)

if peso<=30:
    print(f"{nome} pescisa se cuidar mais {IMC}")
elif  peso<=60:
    print(f"{nome} tudo ok {IMC}")
elif peso<=80:
    print(f"{nome} precisa fazer exercicios e ter uma alimentação regulada {IMC}")
else: peso<=100.0
print(f"{nome} precisa ir urgentemente para o medico {IMC}")
