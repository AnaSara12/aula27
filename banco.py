#CADASTRO DE USUÁRIO E SENHA 
saldo = 0.0 #variavel que guarda saldo do usuário
while True:
    # MENU PRINCIPAL 
    print("Bem vindo!\n Digite 1.cadastrar 2.login 3.ecerrar ")
    #LER A ESCOLHA DO USUÁRIO 
    escolha_menu = int(input())# ler escolha como um usuário

    #se usuário escolher cadastro 
    if escolha_menu == 1:
        #crie um usuário e uma senha com tipo string
        usuario = input("crie um nome de usuário ")
        senha = input("crie uma senha ")
    elif escolha_menu == 2:#se usuário escolher login
        #comparar as inf. cadastradas com uma leitura
        login_usuario = input("Digite seu usuário ")
        login_senha = input("digite sua senha ")
        if login_usuario == usuario and login_senha == senha:
            print("LOGIN REALIZADO COM SUCESSO")
            #SE LOGIN CORRETO , ENTRA NO
            #MENU PRINCIPAL DO APP
            print("BEM VINDO",usuario)
            while True:#ENQUANTO QUE EXIBIRÁ O MENU PRINCIPAL
                print("1.deposito 2. sacar 3. pix 4. extrato 5. encerrar")
                escolha_principal = int(input())
                if escolha_principal == 1: #se usuário escolher depositar
                    #ler valor a ser depositado
                    valor_deposito = float(input())
                    saldo = saldo + valor_deposito #ATUALIZA O VALOR
                    print("NOVO SALDO É",saldo)
                elif escolha_principal == 2 :# SAQUE
                    valor_saque = float(input("Digite o valor do saque "))
                    senha_saque = input("Digite sua senha ")
                    if senha_saque == senha:# se senha correta
                        saldo = saldo - valor_saque #subtrai o valor do saldo 
                    else:
                        print("Senha incorreta")
                elif escolha_principal == 3: #se usuário escolher pix
                    valor_pix = float(input("digite o valor do pix"))
                    senha_pix = input("digite sua senha")
                    if senha_pix == senha:
                        saldo = saldo - valor_pix
                    else:
                        print("senha incorreta")
                elif escolha_principal == 4: #se usuario escolher visualizar 
                    senha_extrato = input("digite sua senha ")
                    if senha_extrato == senha:
                        print("extrato:",saldo)
                    else:
                        print("senha incorreta")
                elif escolha_principal == 5:#encerrar
                    senha_encerrar = input("digite sua senha")
                    if
    else:
        print("USUÁRIO OU SENHA INCORRETOS")

