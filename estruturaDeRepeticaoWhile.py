numero = 1
while numero < 6:
    print(numero)
    numero += 1

soma = 0 
numero = -1
while numero < 6:
    soma += numero
    numero += 1
print(soma)

numero = 12
while numero < 1 or numero > 10:
    numero = int(input('Digite um numero de 1 a 10'))