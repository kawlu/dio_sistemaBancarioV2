import re

def saque(*,numero_saques, LIMITE_SAQUES=3, extrato, saldo, limite):
    
    if numero_saques < LIMITE_SAQUES:
        valor = float(input("\nDigite um valor: "))
        if valor <= saldo:
            if valor <= limite:
                numero_saques+=1
                saldo -= valor
                extrato += f"Saque de R${valor}\n"
                return saldo, extrato, numero_saques
            print(f"\nValor máximo por saque deve ser de até R${limite}")
        else:
            print("\nValor de saque indisponível.")
    else:
        print(f"\nCota diária atingida (3 SAQUES)")
    return saldo, extrato, numero_saques

def deposito(extrato, saldo,/):
    valor = float(input("\nDigite um valor: "))
    saldo += valor
    extrato += f"Deposito de R${valor}\n"
    
    return saldo, extrato
    
def poupanca(extrato, saldo, saldo_poupanca):
    cpf = input("\nInsira seu CPF: ")
    if cpf not in cpfs:
        print("\nCPF não cadastrado.")
        return saldo, extrato, saldo_poupanca
    op = -1
    while op!=0:
        op = int(input(f"\nSaldo da Poupança: R${saldo_poupanca}\nEscolha sua operação\n[1] Depositar\n[2] Sacar\n[0] Sair\n\n"))
        
        if op == 1:
            valor = float(input("Digite o Valor: "))
            if valor > saldo:
                print("Saldo insuficiente para depósito.")
            else:
                saldo_poupanca += valor
                saldo -= valor
                extrato += f"Transferência para Poupança de R${valor}\n"
        elif op == 2:
            valor = float(input("Digite o Valor: "))
            if valor > saldo_poupanca:
                print("Saldo insuficiente para Saque.")
            

    return saldo, extrato, saldo_poupanca
    
def exibir_extrato(saldo,/,*,extrato,saldo_poupanca):
    print("\n======================\nEXTRATO\n")
    print(extrato + f"\nSaldo: R${saldo}\nSaldo da Poupança: R${saldo_poupanca}\n======================")
    
def cadastrarCliente(contas,cpfs):
    padrao_cpf = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$|^\d{11}$'
    
    nome = str(input("\nDigite seu nome completo: "))
    nascimento = str(input("Digite sua data de nascimento (DD/MM/AAAA): "))
    endereco = str(input("Digite seu endereço (logradouro, nro - bairro - cidade/sigla estado): "))
    cpf = str(input("Digite seu CPF (xxx.xxx.xxx-xx): "))
    
    while not re.match(padrao_cpf,cpf):
        cpf = str(input("Formato ou CPF inválido, tente novamente ou digite SAIR: "))
        if cpf == "sair".casefold():
            break
        
    cpf = cpf.replace(".","").replace("-","")
    
    if cpf in cpfs:
        print("\nCPF já cadastrado no sistema.")
        return contas
    else:
        cpfs.append(cpf)
        
        nova_conta = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco,
        "nascimento": nascimento
    }
        contas.append(nova_conta)
        print("\nUsuário cadastrado com sucesso.") 
        
        return contas  
    
def cadastrarContaBancaria(cpfs, contas_correntes):
    cpf = input("\nDigite o CPF do usuário para a nova conta: ")

    if cpf not in cpfs:
        print("\nCPF não cadastrado. Por favor, cadastre o cliente primeiro.")
        return contas_correntes

    agencia = "0001"
    
    numero_conta = len(contas_correntes) + 1
    
    nova_conta_corrente = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "cpf": cpf
    }
    
    contas_correntes.append(nova_conta_corrente)
    
    print(f"\nConta bancária criada com sucesso!\nAgência: {agencia}\nNúmero da Conta: {numero_conta}\nCPF do Titular: {cpf}")
    
    return contas_correntes

menu = """
[1] Depositar
[2] Sacar
[3] Gerenciar Poupança
[4] Exibir Extrato
[5] Cadastrar Novo Cliente
[6] Cadastrar Nova Conta Bancária
[0] Sair

=> """

saldo = 0.0
saldo_poupanca = 0.0
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas = []
contas_correntes = []
cpfs = []

while True:
    
    opcao = int(input(menu))
    
    if opcao == 1:
        saldo, extrato = deposito(extrato, saldo)
        
    elif opcao == 2:
        saldo, extrato, numero_saques = saque(numero_saques=numero_saques, LIMITE_SAQUES=3, extrato=extrato, saldo=saldo, limite=limite)
        
    elif opcao == 3:
        saldo, extrato, saldo_poupanca = poupanca(extrato, saldo, saldo_poupanca)    
         
    elif opcao == 4:
        exibir_extrato(saldo,extrato=extrato,saldo_poupanca=saldo_poupanca)
    
    elif opcao == 5:
        contas = cadastrarCliente(contas,cpfs)
    
    elif opcao == 6:
        contas_correntes = cadastrarContaBancaria(cpfs, contas_correntes)
    
    elif opcao == 0:
        break
    
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")