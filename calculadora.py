# from OperacoesAritimeticas import OperacoesAritimeticas

class Calculadora():

    def soma(self, n1, n2):
        return n1 + n2

    def subtrair(self, n1, n2):
        return n1 - n2

    def multiplicar(self, n1, n2):
        return n1 * n2

    def dividir(self, n1, n2):
        return n1/n2

calculadora = Calculadora()
x = calculadora.soma(1, 2)
print(x)
        
        