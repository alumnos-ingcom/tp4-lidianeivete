################
# Lidiane Ivete da Silva - @lidianeivete
# TP4 - ejercicio 11
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def palindromo(frase):
    palabras = frase.split()
    todo_junto = "".join(palabras)
    invertido = todo_junto[::-1]
    if invertido == todo_junto:
        return True
    else:
        return False
    
def prueba ():
    frase = str(input("escriba una frase: ")).strip().upper()
    resultado = palindromo(frase)
    print (resultado)
    
    
if __name__ == "__main__":
    prueba()

# PRIMER INTENTO:
# 
# frase = str(input("escriba una frase: ")).strip().upper()
# palabras = frase.split()
# todo_junto = "".join(palabras)
# invertido = todo_junto[::-1]
# if invertido == todo_junto:
#     print (True)
# else:
#     print (False)