from flask import Flask
app= Flask (__name__)

@app.route('/bemvindo')
def home():
    return'bem vindo'


@app.route('/calculadora/soma/<int:n1>/<int:n2>')
def soma(n1,n2):
    resultado=n1+n2
    return f'resultado é:{resultado}'

@app.route('/calculadora/subtrair/<int:n1>/<int:n2>')
def subtrair(n1,n2):
    resultado=n1-n2
    return f'resultado é:{resultado}'

@app.route('/calculadora/multiplicação/<int:n1>/<int:n2>')
def multiplicar(n1,n2):
    resultado=n1*n2
    return f'resultado é:{resultado}'

@app.route('/calculadora/divisão/<int:n1>/<int:n2>')
def divisão(n1,n2):
    resultado=n1/n2
    return f'resultado é:{resultado}'
if divisão==0:
     print("não e possivel dividir esse numero por 0")

if __name__ == "__main__":
        app.run(debug=True)



