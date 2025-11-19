def receberDados():
    quantidadeAlunos = int(input("Quantos alunos tem na classe? "))

    nomesAlunos = []
    nota1 = []
    nota2 = []

    for i in range(quantidadeAlunos):
        print("------------------------------------")
        nome = input(f"qual o nome do aluno {i + 1}? ")
        n1 = float(input(f"qual a primeira nota do {nome}? "))
        n2 = float(input(f"qual a segunda nota do aluno {nome}? "))
        
        nomesAlunos.append(nome)
        nota1.append(n1)
        nota2.append(n2)

    return quantidadeAlunos, nomesAlunos, nota1, nota2
    
def calcularMediaAluno(nota1, nota2):
    return [(nota1[i] + nota2[i])/2 for i in range(len(nota1))]

def calcularMediaTurma(medias):
    return sum(medias)/len(medias)


def definirSituacao(medias):
     return [
        "Aprovado!" if m > 6 else "Recuperação!" if m >= 4 else "Reprovado!"
        for m in medias
    ]


def exibirResultado(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao):
    for i in range(len(nomesAlunos)):
        print("-------------\n")
        print(f"Nome: {nomesAlunos[i]}")
        print(f"Nota1: {nota1[i]}")
        print(f"Nota2: {nota2[i]}")
        print(f"Média: {medias[i]}")
        print(f"situação: {situacao[i]}")
        print("\n")

    print("------------------------------")
    print("** Relatório geral da turma **")
    print("------------------------------")
    print(f"Média geral da turma: {mediaTurma}")
    print(f"maior media: {max(medias)}")
    print(f"Menor media: {min(medias)}")
    print(f"Aprovados: {situacao.count('Aprovado!')}")
    print(f"Recuperações: {situacao.count('Recuperação!')}")
    print(f"Reprovados: {situacao.count('Reprovado!') }")
    print("------------------------------")

def main():
    quantidadeAlunos, nomesAlunos, nota1, nota2 = receberDados()
    medias = calcularMediaAluno(nota1, nota2)
    mediaTurma = calcularMediaTurma(medias)
    situacao = definirSituacao(medias)
    exibirResultado(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao)


main()   