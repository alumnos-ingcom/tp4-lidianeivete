# FALTA: METERLO EN UN DEF

dividendo = int(input("ingrese el dividendo: "))
divisor = int(input("ingrese el divisor: "))
cociente = 0
while dividendo > divisor:
    dividendo = dividendo - divisor
    cociente = cociente + 1
print ("el cociente es: ", cociente)
print ("el resto es: ", dividendo)