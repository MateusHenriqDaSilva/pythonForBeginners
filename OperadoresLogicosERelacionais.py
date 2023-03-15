# Operadores Logicos
a = True
b = False
print(a,b)
a and b
a & b
c = a and b
print("A e B são iguais é", c)
a or b
a | b
d = a or b
print("'A' ou 'B' é igual a ", d)
not a
not b

# Operadores Relacionais
5 > 3
5 < 3
5 >= 5
5 <= 3
5 == 3
if 5 > 3:
    print("5 é maior que 3")
print("teste")

if 5 > 6:
    print("5 é maior")
else:
    print("5 não é maior")

n = 3
if n == 4:
    print("não é igual a 4")
else: 
    if n == 3:
        print('n é igual a 3')
    else:
        print('n não é igual a 4 nem a 3')

x = 2
y = 3
if(x > 1) and (y % 2 == 0):
    print("x é maior que 1 e y é par")
else:
    print('uma ou nenhuma das condições foram satisfeitas')