
menu = """"""

(1)
(2)
(3)
(0) 

saldo = 0
limite = 500
extrato = """"""
numero_saque = 0
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

if opçao =="1":
    valor = float(input("Infome o valor do deposito"))
    if valor >0:
        saldo += valor 
        extrato += f"Deposito:RS{valor:.2f}\n"   
else: 
    print("Operação falhou!O valor informado é invalido")

def f(): opção =="2"
valor = float(input("Informe o valor do saque")) 
excedeu_saldo = valor > saldo
excedeu_limite = valor > limite
excedeu_saque =  numero_saque >= LIMITE_SAQUE

if excedeu_saldo:
    print("Operação falhou! Voce não tem saldo suficiente")
elif excedeu_limite:
    print("Operação falhou!O valor do saque excede o limite")
elif excedeu_saque:
    print("Operação falhou!Numero maximo de saque excedido.")

elif valor>0:
    saldo -= valor
extrato += f"Saque: R${valor:.2f}\n"   
numero_saque =+1

def f():
    print("Operação falhou! O valor informado é invalido")

def f():
    print("Extrato")
    print("Não foram realizadas movimentações."if not extrato else extrato)
    print(f"\n saldo: R${saldo:.2f}")
