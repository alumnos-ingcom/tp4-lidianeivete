################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - Ejercicio 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_reintento (ingreso,veces=5):
    
    for i in range (0,veces):
    
      try:
          ingreso = int(ingreso) #ACA DEVERÍA VOLVER A PEDIR EL NUMERO, PERO NO SÉ COMO HACERLO
          break # ACA ME QUEDA LA DUDA SI USO BREAK O PASS
      except ValueError:
          print ("La entrada no es un numero entero.")
                                 
    return "Lo siento, se agotaron los intentos!" 

def prueba():
    ingreso = int(input ("ingrese un numero intero:"))
    resultado = ingreso_reintento
    print (resultado)
    
def ingreso_limitado (ingreso, minimo=1, maximo=10):
    
    if ingreso_entero < maximo and ingreso_entero > minimo :
      return "correcto!"
    else:
      return "El ingreso no está entre los numeros ", minimo," y ", maximo  
    
    
def prueba():    
    ingreso = input ("ingrese un numero entero:")
    resultado = ingreso_limitado
    print (resultado)

if __name__ == "__main__":
    prueba()
    
#
# PRIMER INTENTO:
# 
# for i in range (0,3):
# 
#       try:
#                 ingreso = int(input ("ingrese un numero intero:"))
#                 break
#       except ValueError:
#                 print ("La entrada no es un numero entero.")
# print ("Lo siento, se agotaron los intentos!") 
# 
#                 
# ingreso_entero = int(input("ingrese un numero entre 1 y 10:"))
#    
# if ingreso_entero < 10 and ingreso_entero > 1 :
#   print ("correcto!")
# else:
#   print ("El ingreso no está entre los numeros 1 y 10.")
#                 
#                 
                    
                                        
               
                
        
