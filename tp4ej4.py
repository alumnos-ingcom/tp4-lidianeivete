################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 4
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara_numeros(numero1, numero2):
    if numero1 == numero2:
    return 0
elif numero1 > numero2:
    return 1
else:
    return -1
    
    
def prueba():
    numero1 = int(input("ingrese un numero: "))
    numero2 = int(input("ingrese otro numero: "))
    resultado = compara_numeros (numero1, numero2)
    print resultado

if __name__ == "__main__":
    prueba()


# PRIMER INTENTO:

# numero1 = int(input("ingrese un numero: "))
# numero2 = int(input("ingrese otro numero: "))
# if numero1 == numero2:
#     print (0)
# elif numero1 > numero2:
#     print (1)
# else:
#     print (-1)