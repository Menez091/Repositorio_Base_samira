numero=int(input("digite o numero:"))
onde_começa=int(input("digite o numero que vc quer começar:"))
onde_acaba=int(input("digite em que numero vc quer que acabe:"))


for i in range(onde_começa,onde_acaba):
    print(f"{i} x {numero}={i * numero}")
