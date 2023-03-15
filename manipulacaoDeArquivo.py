with open('c:/Users/Mahends/Desktop/MesaDeEstudos/Legado/Programacao/pythonForBeginners/content/frase1.txt') as text:
    for linha in text:
        print(linha)

with open('c:/Users/Mahends/Desktop/MesaDeEstudos/Legado/Programacao/pythonForBeginners/content/frase1.txt', 'r') as text:
    r = text.readlines()
print(r)

with open('c:/Users/Mahends/Desktop/MesaDeEstudos/Legado/Programacao/pythonForBeginners/content/texto2.txt', 'w') as tex:
    tex.write('Ola me chamo mateus tudo bem? sim')
