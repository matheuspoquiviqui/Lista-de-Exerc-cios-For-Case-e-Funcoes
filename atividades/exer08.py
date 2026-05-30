#Faça uma calculadora usando match case.

print("-- CALCULADORA --")
print("1 Soma | 2 Subtração | 3 Multiplicação | 4 Divisão ")

operacao = int(input("Escolha uma opção: "))

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

match operacao:
    case 1:
        print("Resultado:", num1 + num2)
    case 2:
        print("Resultado:", num1 - num2)
    case 3:
        print("Resultado:", num1 * num2)
    case 4:
        print("Resultado:", num1 / num2)
    case _:
        print("Opção inválida")


