# Peça um número e mostre a tabuada de 1 a 10 usando for

print("-- TABUADA DE 1 A 10 --")

numero = int(input("Digite um número: "))

for i in range(1, 11):
   resultado = numero * i
   print(numero, "x", i, "=", resultado)