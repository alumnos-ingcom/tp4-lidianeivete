################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 10
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def factores_primos (numero):
    primos = []
    for i in range (2,numero+1):
        while numero % i == 0:
            primos.append (i)
            numero = numero / i
    return "sus factores primos son: ", primos

def prueba ():
    numero = int(input("ingrese un numero: "))
    resultado = factores_primos (numero):
    print (resultado)    

if __name__ == "__main__":
    prueba()

# PRIMER INTENTO:

# numero = int(input("ingrese un numero: "))
# primos = []
# for i in range (2,numero+1):
#     while numero % i == 0:
#         primos.append (i)
#         numero = numero / i
# print ("sus factores primos son: ", primos)
# 
