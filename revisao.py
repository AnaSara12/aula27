#ler entrada de usuario
escolha_menu = int(input("escolha opção")) #variavel que guarda qual opção do menu
alunos = []
if escolha_menu == 1:#se ele escolher cadastro
    cont = 0#variavel que controla a repetição
    escolha_usuario = int(input("escolha quantos aluno vai se cadastrar"))#variavel que guarda quantas vezes o codigo vai rodar
    
    while cont < escolha_usuario:
        nome = input(("digite o nome "))#ARMAZENAR o nome do aluno
        nota1 = float(input("digite nota 1"))# 4 notas do aluno5
        nota2 = float(input("digite nota 2"))
        nota3 = float(input("digite nota 3"))
        nota4 = float(input("digite nota 4"))

        faltas = int(input("digite faltas"))
        #caculo da média
        media = (nota1+nota2+nota3+nota4)/4

        #logica da situacao
        if faltas >31:
            situacao = "reprovado por faltas"
        elif media >= 8:
            situacao = "aprovado"
        elif media >= 5: #recuperação
            recuperacao = float(input())#ler a nota da recuperação
            if recuperacao >= (10-media):
                situacao = "aprovado na recuperação"
            else:
                situacao = "reprovado na recuperação"
        else:
            situacao = "reprovado por média"
        #enviar os dados do aluno para a lista (aluno)
        alunos.append([nome,faltas, media, situacao])
        cont += 1
        #relatorio
print(alunos)
