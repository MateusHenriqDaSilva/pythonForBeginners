# Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução

# 1. Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão
def lerNumeros(mensagem):
    valor = int(input(mensagem))
    return valor

def adicao(valor1, valor2):
    adicao = valor1 + valor2
    return adicao

def subtracao(valor1, valor2):
    subtracao = valor1 - valor2
    return subtracao

def divisao(valor1, valor2):
    divisao = valor1 / valor2
    return divisao

def multiplicacao(valor1, valor2):
    multiplicacao = valor1 * valor2
    return multiplicacao

def mostrarValor(valor):
    print("operacao: ", valor)

if __name__ == "__main__":
    valor1 = lerNumeros("Digite o valor1: ")
    valor2 = lerNumeros("Digite o valor2: ")
    mostrarValor(adicao(valor1, valor2))
    mostrarValor(subtracao(valor1, valor2))
    mostrarValor(divisao(valor1, valor2))
    mostrarValor(multiplicacao(valor1, valor2))

# 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, 
# o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula 
# DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: 
# LITROS_USADOS = DISTANCIA / 12. O 
# programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem 
def lerValores(mensagem):
    valor = int(input(mensagem))
    return valor

def calcularDistancia(tempo, velocidade):
    distancia = tempo * velocidade
    return distancia

def litrosUsados(distancia):
    litrosUsadosViagem = distancia / 12
    return litrosUsadosViagem

def mostrarValor(tempo, velocidade, distancia, litrosUsadosViagem):
    print("tempo: ", tempo)
    print("velocidade: ", velocidade)
    print("distancia: ", distancia)
    print("litrosUsadosViagem: ", litrosUsadosViagem)

if __name__ == "__main__":
    tempo = lerValores("Tempo gasto: ")
    velocidade = lerValores("Velocidade: ")
    distancia = calcularDistancia(tempo, velocidade)
    litrosUsadosViagem = litrosUsados(distancia)