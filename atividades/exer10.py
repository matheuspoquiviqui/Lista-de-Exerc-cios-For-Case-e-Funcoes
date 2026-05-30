#Crie uma função que mostre a tabuada do número digitado.

print("-- MULTIPLICAÇÕES --")

def Tabuada (numero):
    for i in range(1,11):
        resultado = numero * i
        print (numero,"x",i,"=",resultado)

num1 = int(input("Digite um número: "))

print (Tabuada(num1))