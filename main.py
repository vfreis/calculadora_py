import os
from flask import Flask, request, jsonify
# from math import sqrt
from calculadora import Calculadora


app = Flask(__name__)


class Abort (Exception):
    pass

@app.route('/calculadora')
def calculadoraWeb():
    valor1 = request.args.get('v1')
    valor2 = request.args.get('v2')
    operacao = request.args.get('operacao')

    try:
        v1 = float(valor1)
    except ValueError:
        Abort(404)

    try:
        v2 = float(valor2)
    except ValueError:
        Abort(404)

    calcular = Calculadora()


    if(operacao == 'somar'):
        resultadoCalculado = calcular.somar(v1, v2)

    elif(operacao == 'dividir'):
        if (v2 == 0):
            Abort(402)
        else:
            resultadoCalculado = calcular.dividir(v1, v2)

    elif(operacao == 'subtrair'):
        resultadoCalculado = calcular.subtrair(v1, v2)

    elif(operacao == 'multiplicar'):
        resultadoCalculado = calcular.multiplicar(v1, v2)
    else:
        Abort(404)

    return str(resultadoCalculado)



