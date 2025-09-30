from flask import Flask
app= Flask (__name__)

@app.route('/bemvindo/<name>')
def bemvindo(name):
    return f'bem vindo {name}'

if __name__ == "__main__":
        app.run(debug=True)










