#DECLARAR UMA FUNÇÃO
def saudacoes(hora_do_dia): #exibir a saudação correspondente a hora
    #DAR BOM DIA
     if (hora_do_dia >= 0) and (hora_do_dia <= 12):
          print("BOM DIAA!")
     elif (hora_do_dia >= 13) and (hora_do_dia <=18 ):
          print("BOA TARDE!!!")
     else:
          print("BOA NOITE!!!") 

#FORA DA FUNÇÃO
#PEÇO PARA O USUÁRIO DIZER A HORA ATUAL
resposta = int(input("Digite que horas são:\n"))
#CHAMO A FUNÇÃO PASSANDO PARA ELA O PARAMETRO OBRIGATORIO

saudacoes(resposta)