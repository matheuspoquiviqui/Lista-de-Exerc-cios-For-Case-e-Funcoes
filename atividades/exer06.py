''' 
Adivinhação:
Defina o número secreto como o número 7.
Peça um número do usuário para que tente adivinhar até acertar.
'''

print(" -- ADIVINHE O NÚMERO --")

numero_secreto = 7
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")

    else:
        print("Número errado, tente novamente!");