################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 9
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def verifica_primos (numero):
    contador = 0
    divisor = 0
    while numero != divisor :
        divisor = divisor + 1
        if numero % divisor == 0 :
            contador = contador + 1
        else:
            contador = contador
            
    if contador == 2:
        return True
        
    else:
        return False
    
def prueba ():
    numero = int(input("ingrese el numero: "))
    resultado = verifica_primos (numero):
    print resultado

if __name__ == "__main__":
    prueba()
        
# PRIMER INTENTO:

# numero = int(input("ingrese el numero: "))
# contador = 0
# divisor = 0
# while numero != divisor :
#     divisor = divisor + 1
#     if numero % divisor == 0 :
#         contador = contador + 1
#     else:
#         contador = contador
#         
# if contador == 2:
#     print(True)
#     
# else:
#     print (False)



        
        

