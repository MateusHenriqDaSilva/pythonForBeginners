# 1. Leia a idade do usuário e classifique-o em:
# – Criança – 0 a 12 anos
# – Adolescente – 13 a 17 anos
# – Adulto – acima de 18 anos
# -Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida
def lerIdade(mensagem):
    valor = int(input(mensagem))
    return valor

def verificaIdade(idade):
    if 0 < idade < 12:
        return print("Criança")
    elif 13 < idade < 17:
        return print("Adolescente")
    elif idade > 18:
        return print("Adulto")
    else:
        return print("invalido")

if __name__ == "__main__":
    idade = lerIdade("digite a idade: ")
    verificaIdade(idade)
# 2. Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética.
#  Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
# – Se a média for maior ou igual 0.0 e menor ou igual 4.0, o aluno está reprovado
# – Se a média for maior que 4.0 e menor do que 6.0, o aluno pegou exame
# – Se a média for maior ou igual a 6.0, o aluno está aprovado
# – Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado
def calcularMedia(m1,m2,m3):
    media = m1 + m2 + m3
    return media

def lerNotas(mensagem):
    valor = int(input(mensagem))
    return valor

def verificaMedia(media):
    if 0 < media < 4:
        return print("Aluno reprovado!!")
    elif 4 < media < 6 :
        return print("pego exame!!!")
    elif media > 6: 
        return print("Aluno aprovado.")

if __name__ == "__main__":
    m1 = lerNotas("Digite a primeira nota: ")
    m2 = lerNotas("Digite a segunda nota: ")
    m3 = lerNotas("Digite a terceira nota: ")
    media = calcularMedia(m1, m2, m3)
    verificaMedia(media)