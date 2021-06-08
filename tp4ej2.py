################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - Ejercicio 2
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#CORREGIR: TODAVIA NO FUNCIONA CON NEGATIVOS

def suma_lenta (numero1, numero2):
    while numero1 != 0:
     numero1 = numero1 - 1
     numero2 = numero2 + 1
     return numero2

def prueba():
    numero1 = int(input("ingrese el primer numero:"))
    numero2 = int(input("ingrese el segundo numero:"))
    resultado = suma_lenta(numero1, numero2)
    Print resultado

if __name__ == "__main__":
    prueba()
    
    
# PRIMER INTENTO:
#     
# numero1 = int(input("ingrese el primer numero:"))
# numero2 = int(input("ingrese el segundo numero:"))
# 
# while numero1 != 0:
#     numero1 = numero1 - 1
#     numero2 = numero2 + 1
#     print (numero2)