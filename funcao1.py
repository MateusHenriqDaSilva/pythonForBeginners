# funcao sem parametro e retorno
def mensagem():
    print('texto da funcao')

mensagem()
mensagem()
mensagem()

# Funcao com parametro
def mensagem(texto):
    print(texto)

mensagem('texto1')
mensagem('texto2')
mensagem('texto3')

def soma(a, b):
    print(a + b)

soma(2, 3)
soma(3, 3)
soma(1, 3)

# Funcao com parametro e retorno
def soma(a, b):
    return a + b

soma(3,2)
r = soma(3, 2)
print(r)

def calcularEnergiaPotencialGravitacional(m, h, g = 10):
    e = g * m * h
    return e
calcularEnergiaPotencialGravitacional(30,12)