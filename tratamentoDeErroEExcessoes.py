while True:
    try:
        n = int(input("Digite um numero inteiro: "))
    except:
        print('valor invalido')
    else:
        print(f'valor digitado é {n}')
        break

while True:
    try:
        p = int(input("Digite um numero inteiro: "))
    except ValueError:
        print('valor invalido')
    except KeyboardInterrupt:
        print(f'valor digitado é {p}')
        break
    else:
        print(f'Valor digitado é {p}')
        break
    