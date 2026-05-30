'''
Crie um menu que faça:
1 - Somar
2 - Subtrair
3 - Sair
'''

opcao = 0

print("-- CALCULADORA DE SOMA E SUBTRAÇÃO --")

while opcao !=3:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        print("Resultado:", num1 + num2)

    elif opcao == 2: 
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número: "))
        print("Resultado:", num1 - num2)

print("Programa encerrado!")