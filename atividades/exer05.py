'''
Primeiros usos do While:

Peça números ao usuário e mostre a soma total.
O programa só para quando o usuário digitar 0.

'''

print(" -- SOMA DE NÚMEROS --")

soma = 0
numero = 1

while numero !=0:
    numero = int(input("Digite um número para soma, ou aperte 0 para sair: "))
    soma = soma + numero

print("Soma total:", soma)