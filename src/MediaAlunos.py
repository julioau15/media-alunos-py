import json

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
        print(f"Média: {medias[i]:2f}")
        print(f"situação: {situacao[i]}")
        print("\n")

    print("------------------------------")
    print("** Relatório geral da turma **")
    print("------------------------------")
    print(f"Média geral da turma: {mediaTurma:2f}")
    print(f"maior media: {max(medias)}")
    print(f"Menor media: {min(medias)}")
    print(f"Aprovados: {situacao.count('Aprovado!')}")
    print(f"Recuperações: {situacao.count('Recuperação!')}")
    print(f"Reprovados: {situacao.count('Reprovado!') }")
    print("------------------------------")


def salvarTxt(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao):
    with open("relatorio.txt","w") as arquivo:
        arquivo.write("RELATÓRIO FINAL\n")
        arquivo.write("----------------------\n")

        arquivo.write(
            "------------------------------"
            "** Relatório geral da turma **"
            "------------------------------"
            f"Média geral da turma: {mediaTurma:2f} |"
            f"maior media: {max(medias)} |"
            f"Menor media: {min(medias)} |"
            f"Aprovados: {situacao.count('Aprovado!')} |"
            f"Recuperações: {situacao.count('Recuperação!')} |"
            f"Reprovados: {situacao.count('Reprovado!') } \n|"
        )

        for i in range(len(nomesAlunos)):
            arquivo.write(
                f"Nome: {nomesAlunos[i]} |"
                f"Nota 1: {nota1[i]} |"
                f"Nota 2: {nota2[i]} |"
                f"Média: {medias[i]} |"
                f"Situação: {situacao[i]} |\n"
            )

    print("Arquivo relatorio.txt gerado com sucesso!")

def salvarJson(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao):
    dados = []

    for i in range(len(nomesAlunos)):
        dados.append({
            "Nome": nomesAlunos[i],
            "Nota 1": nota1[i],
            "Nota 2": nota2[i],
            "Média": medias[i],
            "Situação": situacao[i]
        })

    relatorioGeral = {
        "quantidadeAlunos": len(nomesAlunos),
        "Média geral da turma": mediaTurma,
        "maior media": max(medias),
        "Menor media": min(medias),
        "Aprovados": situacao.count('Aprovado'),
        "Recuperações": situacao.count('Recuperação!'),
        "Reprovados": situacao.count('Reprovado!'),
        "alunos": dados

    }

    with open('relatorio.json', 'w') as arquivo:
        json.dump(relatorioGeral, arquivo, indent = 4, ensure_ascii=False)

    print("Arquivo relatorio.txt gerado com sucesso!")

def escolherFormato(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao):
    print("\n Deseja salvar o relatorio como:")
    print("1 - TXT")
    print("2 - JSON")
    print("3 - Não salvar")
    opcao = input("Escolha: ")

    if opcao == "1":
        salvarTxt(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao)
    elif opcao == "2":
        salvarJson(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao)
    else:
        print("Finalizado!")


def main():
    quantidadeAlunos, nomesAlunos, nota1, nota2 = receberDados()
    medias = calcularMediaAluno(nota1, nota2)
    mediaTurma = calcularMediaTurma(medias)
    situacao = definirSituacao(medias)
    exibirResultado(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao)
    escolherFormato(nomesAlunos, nota1, nota2, medias, mediaTurma, situacao)


main()   