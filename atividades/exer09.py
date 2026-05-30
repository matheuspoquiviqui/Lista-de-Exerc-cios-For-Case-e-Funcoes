#Crie uma função chamada somar que some dois números.

def Somar (a,b):
    resultado = a + b
    return resultado

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

print ("Resultado:", Somar(num1,num2))