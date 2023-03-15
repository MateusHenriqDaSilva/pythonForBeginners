# 1. Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra 
# estrutura de repetição para somar todos os valores digitados

# 3. Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                    [3, 1, 5]])
import numpy as np

def receberNumero(mensagem):
    valor = int(input(mensagem))
    return valor


if __name__ == "__main__":
    lista = np.empty(5)
    soma = 0
    for contador in range(0,5):
        lista[contador] = receberNumero("digite o numero: ")
    
    for contador in range(0,5):
        soma = soma + lista[contador]
print("soma: ", soma)
# 2. Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, fazendo a leitura dos valores por meio de uma estrutura de repetição. 
# Depois, crie uma nova estrutura de repetição para somar todas as notas e retornar a média
dicionario = {}
for item in range(0,3):
    nome = input("digite o nome: ")
    valor = int(input("digite o valor: "))
    dicionario[nome] = valor

dicionario.values()
print(dicionario)
# 3. Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz
# matriz = np.array([[3, 4, 1],
#                    [3, 1, 5]])

matriz = np.array([[3, 4, 1],[3, 1, 5]])
for item in matriz:
    print(item)