################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 7
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def resta_sucesiva (dividendo,divisor):
    cociente = 0
    while dividendo > divisor:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    return "el cociente es: ", cociente, " y el resto es: ", dividendo
    
def prueba():
    dividendo = int(input("ingrese el dividendo: "))
    divisor = int(input("ingrese el divisor: "))
    resultado = resta_sucesiva (dividendo,divisor)
    print (resultado)

if __name__ == "__main__":
    prueba()

#PRIMER INTENTO:
# 
# dividendo = int(input("ingrese el dividendo: "))
# divisor = int(input("ingrese el divisor: "))
# cociente = 0
# while dividendo > divisor:
#     dividendo = dividendo - divisor
#     cociente = cociente + 1
# print ("el cociente es: ", cociente)
# print ("el resto es: ", dividendo)