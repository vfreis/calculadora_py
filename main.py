import os
from flask import Flask, request, jsonify, render_template, url_for
# from math import sqrt
from calculadora import Calculadora

app = Flask(__name__)

# para nao ordenar json
app.config['JSON_SORT_KEYS'] = False

class Abort (Exception):
    pass


@app.route('/')
def init():
    return render_template('index.html')

@app.route('/calculadora', methods = ['POST', 'GET'])
def calculadoraWeb():
    valor1 = request.form['input_v1']
    valor2 = request.form['input_v2']
    operacao = request.form['operacao']

    try:    
        v1 = float(valor1)
    except ValueError:
        Abort(404)

    try:
        v2 = float(valor2)
    except ValueError:
        Abort(404)


    calcular = Calculadora()


    if(operacao == 'Somar'):
        resultadoCalculado = calcular.somar(v1, v2)

    elif(operacao == 'Dividir'):
        if (v2 == 0):
            Abort(402)
        else:
            resultadoCalculado = calcular.dividir(v1, v2)

    elif(operacao == 'Subtrair'):
        resultadoCalculado = calcular.subtrair(v1, v2)

    elif(operacao == 'Multiplicar'):
        resultadoCalculado = calcular.multiplicar(v1, v2)
    
    elif(operacao == 'Potencia'):
        resultadoCalculado = calcular.potencia(v1, v2)

    else:
        Abort(404)

    return jsonify(Valor1 = valor1, Valor2 = valor2, Operacao = operacao, Resultado = str(resultadoCalculado))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host= 'localhost', port = port)

    



