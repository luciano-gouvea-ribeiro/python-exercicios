''' Criando um Sistema Bancario '''

menu = ('''
     Menu
 [0] Depositar
 [1] Saquar
 [2] Extrato
 [3] Sair
'''
)

saldo = 0
deposito = 0
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUE = 3
VALOR_MAXIMO_DE_SAQUE = 500

while True:
    opcao_do_usuario = int(input(menu))



    if opcao_do_usuario == 0:
        print('Deposito.')
        valor_deposito = float(input('Digite o valor que quer Depositar: '))
            
        if valor_deposito <= 0:
            print('Operação Falhou: Valor invalido para Deposito.')
        else:
            saldo += valor_deposito
            extrato += f'Você Depositou R$ {valor_deposito:.2f}\n'
   
        
    elif opcao_do_usuario == 1:
        numero_de_saques += 1
        print('Saquar.')
        valor_de_saque = int(input('Digite o valor que quer Saquar: '))
        
        if valor_de_saque > VALOR_MAXIMO_DE_SAQUE:
            print('Você não pode sacar mais de R$ 500.')
        elif numero_de_saques > LIMITE_DE_SAQUE:
            print('Você nao pode efetuar mais de 3 saques. ')
        elif valor_de_saque > saldo:
            print('Você não tem saldo suficiente para saquar dá sua conta.')
        elif valor_de_saque < 0:
            print('Operação Falhou: Você não pode saquar valores negativos.')
        
        else:
            saldo -= valor_de_saque
            extrato += f'Você saquou dá sua conta R$ {valor_de_saque:.2f}\n'

    
    elif opcao_do_usuario == 2:
        print('######## Extrato ########')
        print('Não foram realizadas Movimentações.'if not extrato else extrato )
        print(f'Seu saldo da conta atual é R$ {saldo:.2f}')
    
    elif opcao_do_usuario == 3:
        print('Obrigado pela vizita volte sempre.')
        break
    else:
       print('Operação Falhou.. Verficar se esta escolhendo a opção correta.')
       