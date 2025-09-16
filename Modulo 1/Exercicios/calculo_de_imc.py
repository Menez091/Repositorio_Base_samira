nome=input("qual seu nome ?")
peso=float(input("qual o seu peso em kg?"))
altura=float(input("qual sua altura em metros?"))
imc=peso/(altura * altura)

if imc <18.5:
    print(f"{nome} voce está abaixo do peso e seu IMC é {imc},precisa se cuidar mais!")
elif imc <24.9:
    print(f"{nome} voce está com o peso normal e seu IMC é {imc},tudo ok!")
elif imc <29.9:
    print(f"{nome} voce está com sobre peso e seu IMC é {imc}, precisa ir ao medico! ")
elif imc <34.9:
    print(f"{nome} voce está com obsidade grau 1 e seu IMC é {imc},precisa ir urgentemente para o medico!")
elif imc <39.9:
    print(f"{nome} voce está com obsidade grau 2 e seu IMC é {imc},precisa ir urgentemete para o medico! ")
else:
    print(f"{nome} tome cuidado seu IMC e {imc},precisa se cuidar muito! ")
