'''
Construya un programa en Python que solicite a un
usuario un número entero positivo, y entregue como
resultado el número invertido
'''
#DATOS DE ENTRADA
numero_ingresado = int(input("Ingrese un número mayor a cero: "))
revertir = 0

#PROCESAMIENTO
if numero_ingresado > 0 :
    while numero_ingresado > 0:
        residuo = numero_ingresado % 10
        revertir = (revertir * 10) + residuo
        numero_ingresado //= 10

#SALIDAS
    print('El inverso del número ingresado es: ', revertir)
else:
    print("El número ingresado no es valido.")