#Peça 5 números ao usuário e mostre a soma utilizando for

print("-- SOMA DE 5 NÚMEROS --")

soma = 0

for i in range(5):
    numero = float(input("Informe o número para soma: "))
    soma = numero + soma

print ("Resultado:", soma)