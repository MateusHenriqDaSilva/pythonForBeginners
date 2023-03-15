# 1. Ler 5 notas e informar a média
import numpy

def lerNotas(mensagem):
    nota = int(input(mensagem))
    return nota

if __name__ == "__main__":
    nota = numpy.empty(5)
    contador = 0
    soma = 0
    while contador < 5: 
        nota[contador] = lerNotas("digite o valor da nota ")
        soma = soma + nota[contador]
        contador = contador + 1
    print("soma: ", soma)

# 2. Imprimir a tabuada do número 3 (3 x 1 = 1 – 3 x 10 = 30)
contador = 0
while contador <= 10:
    print("3 x ", contador, " = ", 3*contador)
    contador = contador + 1