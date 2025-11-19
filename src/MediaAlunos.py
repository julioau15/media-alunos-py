quantidadeAlunos = 0
nomesAlunos = []
nota1 = []
nota2 = []
mediaAlunos = []
situacao = []

def receberDados():
    global quantidadeAlunos
    global nomesAlunos
    global nota1
    global nota2
    quantidadeAlunos = int(input("Quantos alunos tem na classe? "))

    nomesAlunos = [None]* quantidadeAlunos
    nota1 = [None]* quantidadeAlunos
    nota2 = [None]* quantidadeAlunos

    j = 1
    for i in range(quantidadeAlunos):
        print("------------------------------------")
        nomesAlunos[i] = input(f"qual o nome do aluno {j}? ")
        nota1[i] = float(input(f"qual a primeira nota do {nomesAlunos[i]}? "))
        nota2[i] = float(input(f"qual a segunda nota do aluno {nomesAlunos[i]}? "))
        print("------------------------------------")
        j += 1

    calcularMedia()
    
def calcularMedia():
    global nota1
    global nota2
    global mediaAlunos
    global quantidadeAlunos

    mediaAlunos = [None]*quantidadeAlunos

    for i in range(quantidadeAlunos):
        mediaAlunos[i] = (nota1[i] + nota2[i])/2
    
    definirSituacao()

def definirSituacao():
    global mediaAlunos
    global quantidadeAlunos
    global situacao

    situacao = [None]*quantidadeAlunos

    for i in range(quantidadeAlunos):
        if mediaAlunos[i] > 6:
            situacao[i] = "Aprovado!"
        elif mediaAlunos[i] >= 5:
            situacao[i] = "Recuperação!"
        else:
            situacao[i] = "Reprovado!"

    exibirResultado()


def exibirResultado():
    global nomesAlunos
    global nota1
    global nota2
    global mediaAlunos
    global quantidadeAlunos
    global situacao

    for i in range(quantidadeAlunos):
        print("-------------")
        print(f"Nome: {nomesAlunos[i]}")
        print(f"Nota1: {nota1[i]}")
        print(f"Nota2: {nota2[i]}")
        print(f"Média: {mediaAlunos[i]}")
        print(f"situação: {situacao[i]}")
        print("-------------")
            
    

    
receberDados()