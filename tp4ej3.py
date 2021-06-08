################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 3
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit (centigrados):
    fahrrenheit = (9/5*(centigrados)+32)
    return fahrrenheit

def convertir_ a_centigrados (fahrrenheint):
    centigrados = (5/9*((fahren)-32))
    return centigrados

def prueba():
    centigrados = float(input("cuantos grados centigrados a transformar? "))
    print (centigrados, " °C es equivalente a " ,fahrrenheit," °F.")

def prueba():
    fahrrenheit = float(input("cuantos grados fahrrenheit a transformar?"))
    print(fahrrenheit ," °F es equivalente a ",centigrados, "°C.")

if __name__ == "__main__":
    prueba()
    
# ABAJO EL PRIMER INTENTO:
# 
# centigrados = float(input("cuantos grados centigrados a transformar? "))
# fahrenheit = (9/5*(centigrados)+32)
# print (centigrados, " °C es equivalente a " ,fahrenheit," °F.")
# 
# fahren = float(input("cuantos grados fahrenheit a transformar?"))
# centi = (5/9*((fahren)-32))
# print(fahren ," °F es equivalente a ",centi, "°C.")

