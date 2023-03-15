# Crie uma classe chamada aluno com os seguintes atributos:
# – Nome
# – Nota 1
# – Nota 2
# – Crie um construtor para a classe (__init__)
# Crie as seguintes funções (métodos):
# – Calcula média, retornando a média aritmética entre as notas
# – Mostra dados, que somente imprime o valor de todos os atributos
# – Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
# Crie dois objetos (aluno1 e aluno2) e teste as funções

class Aluno():
    def __init__(self,nome, nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0
    
    def calculaMedia(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media
    
    def mostrarDados(self):
        print("Nome: ", self.nome)
        print("Nota1: ", self.nota1)
        print("Nota2: ", self.nota2)
        print("Meida: ", self.media)

    def resultado(self):
        if self.media > 7:
            print("Aprovado!!!")
        elif 4 < self.media < 7:
            print("Ficou de exame!!!")
        else:
            print("Reprovado")

aluno1 = Aluno('Mateus', 10, 10)
aluno1 = Aluno('Mateus', 5, 5)
aluno1.calculaMedia()
aluno1.mostrarDados()
aluno1.resultado()
