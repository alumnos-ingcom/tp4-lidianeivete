################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 5
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo (ingreso):
    if ingreso == 0:
    return ("el ingreso es igual a cero.")
elif ingreso > 0:
    return "el ingreso es positivo."
else:
    return "el ingreso es negativo."

def prueba():
    ingreso = int(input("ingrese un numero: "))
    resultado = signo (ingreso)
    print resultado
    
if __name__ == "__main__":
    prueba()    


# PRIMER INTENTO:
#     
# ingreso = int(input("ingrese un numero: "))
# if ingreso == 0:
#     print ("el ingreso es igual a cero.")
# elif ingreso > 0:
#     print ("el ingreso es positivo.")
# else:
#     print ("el ingreso es negativo.")
    