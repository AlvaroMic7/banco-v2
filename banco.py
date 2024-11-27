def deposito(saldo, extrato, /):
    deposito = float(input("Insira o valor que deseja depositar: "))
    saldo += deposito
    extrato += f"foi depositado: {deposito:.2f}\n"
    return saldo, extrato
def saque(*, saldo, extrato, contador_saquediario, limite_saque):

    if contador_saquediario<3:
        sacar = float(input("quanto deseja sacar?"))
        if sacar <= limite_saque:
            if sacar <= saldo:
                saldo -= sacar
                contador_saquediario += 1
                extrato += f"foi sacado: R${sacar:.2f}\n"
            else: 
                print("Voce nao possui saldo suficiente!")
        else:
            print("Seu saque deve ser menor que R$500,00!")
    else:
        print("Voce atingiu o limite de Saques Diarios!")
    return saldo, extrato, contador_saquediario
def imprimir_extrato(extrato, saldo):
    if extrato == "":
        extrato = "Nao foram realizadas movimentacoes"

    print("------EXTRATO--------")
    print(extrato)
    print(f"Voce possui R${saldo:.2f}")
    print("---------------------")


def menu_login_contabancaria():

    menu_contabancaria = """
    ##########-MENU-##########
    [1]-Entrar conta bancaria
    [2]-Criar conta bancaria
    [3]-Voltar
    ##########################
    """
    print(menu_contabancaria)
    opcao = int(input("Insira a Opção: "))
    return opcao
def menu_logado():
    saldo = 0
    contador_saquediario = 0
    limite_saque = 500
    extrato = ""
    menu_logado = """
    ##########-MENU-##########
        [1]-Deposito
        [2]-Saque
        [3]-Extrato
        [4]-Voltar
    ##########################
    """


    while True:
    
        print(menu_logado)
        opcao = int(input("Insira a Opção: "))
        if opcao == 1:
            saldo, extrato = deposito(saldo, extrato)        
        elif opcao == 2:
            saldo, extrato, contador_saquediario = saque(saldo=saldo, extrato=extrato, contador_saquediario=contador_saquediario, limite_saque=limite_saque)
        elif opcao == 3:
            imprimir_extrato(extrato, saldo)
        elif opcao == 4:
            break

def logar_usuario(usuarios):
    cpf = int(input("Digite seu cpf: "))
    for i, usuario in enumerate(usuarios):
        if usuarios[i][2] == cpf:
            return True
        
    return False
def criar_usuario(usuarios):
    nome = input("Digite seu nome: ")
    data_de_nascimento = input("Digite sua Data de Nascimento: ")
    cpf = int(input("Digite seu cpf: "))
    endereco = input("Digite seu endereco: ")

    usuario_novo = [nome, data_de_nascimento, cpf, endereco]
    usuarios.append(usuario_novo)

    return usuarios

def logar_contabancaria(contas):
    cpf = int(input("Digite seu cpf: "))
    numero_da_conta = int(input("Digite numero da sua conta: "))
    for i, conta in enumerate(contas):
        if contas[i][2] == cpf and contas[i][1] == numero_da_conta:
            return True
        
    return False
    #deve retornar verdadeiro ou falso se conseguir logar
def criar_contabancaria(contas, quantidade_contas):
    cpf = int(input("Digite seu cpf: "))
    conta_nova = ["0001", quantidade_contas+1, cpf]
    contas.append(conta_nova)
    print(f"sua conta: {conta_nova}")

    return contas
menu_inicial = """
##########-MENU-##########
   [1]-Acessar Usuario
   [2]-Criar Usuario
   [3]-Listar Usuario
   [4]-Sair
##########################
"""
usuarios = [
    ["adm", "12/09/2000", 12345678910, "Rua padre estevao, 269 - Vila Matoso - Russas/CE"],
]
contas = [
    ["0001", 1, 12345678910],
]
quantidade_contas = 1

while True:

    print(menu_inicial)
    opcao = int(input("Insira a Opção: "))

    if opcao == 1: #  ACESSAR USUARIO

        login = logar_usuario(usuarios)

        if login:
            while True:
                print("Logado com sucesso!")
                opcao = menu_login_contabancaria()
                if opcao == 1: 
                    login = logar_contabancaria(contas) 
                    if login:
                        menu_logado()
                    else:
                        continue
                elif opcao == 2: 
                    contas = criar_contabancaria(contas, quantidade_contas)
                    quantidade_contas += 1
                elif opcao == 3:
                    break
                else:
                    print("Selecione uma opcao correta!")                        
        else:
            print("Login nao encontrado!")
            continue
    elif opcao == 2: # CRIAR USUARIO
        usuarios = criar_usuario(usuarios)
    elif opcao == 3: # LISTAR USUARIO
        print(usuarios)
    elif opcao == 4: # SAIR
        break 
    else:
       print("Selecione uma opcao correta!")

