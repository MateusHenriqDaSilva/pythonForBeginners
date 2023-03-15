# 1. Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista
#  (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
# – ValueError: se o usuário digitar um caracter
# – ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# – IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# – KeyboardInterrupt: caso o usuário interrompa a execução
# 2. Mostre uma mensagem personalizada na ocorrência de cada um desses erros

import numpy

lista = []

try:
    lista.append(float(input("digite o valor1")))
    lista.append(float(input("digite o valor2")))
    divisao = lista[0] / lista[1]
except ValueError:
    print("Digitou um caracter")
except ZeroDivisionError:
    print("Digitou um valor nao divisivel")
except IndexError:
    print("Posicao se encontra divergente")
except KeyboardInterrupt:
    print("Voce parou a execução")
else:
    print("Divisao: ", divisao)