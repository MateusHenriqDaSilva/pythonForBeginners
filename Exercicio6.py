# 1. Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius
# – Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# – Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# – Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão
def lerValor(mensagem):
    valor = int(input(mensagem))
    return valor

def calcularValor(C):
    F = (9 * C + 160) / 5
    return F

def mostrarValor(f):
    print("Fahrenheit: ", f)

if __name__ == "__main__":
    c = lerValor("digite o valor")
    f = calcularValor(c)
    mostrarValor(f)

# 2. Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível 
# obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de 
# litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem
# – Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# – Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
# – Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
# – Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
def lerValor(mensagem):
    valor = int(input(mensagem))
    return valor

def calcularDistancia(t,v):
    d = t * v
    return d

def calcularLitro(d):
    litrosUsados = d / 12
    return litrosUsados

def mostrarValor(t,v,d,l):
    print("tempo: ", t)
    print("velocidade: ", v)
    print("distancia: ", d)
    print("litrosUsados: ", l)

if __name__ == "__main__":
    tempo = lerValor("digite o tempo: ")
    velocidade = lerValor("digite o velocidade: ")
    distancia = calcularDistancia(tempo, velocidade)
    litrosUsados = calcularLitro(distancia)
    mostrarValor(tempo,velocidade,distancia,litrosUsados)

    