
###################### Ejercicio 1 ##############################
'''
Construya un programa en Python que imprima por
pantalla la raíz cuadrada de los números múltiplos de 3 de
la siguiente lista de valores
lista = [10,33,9,14,18,114,12,21,50,55,60]
'''

#IMPORTAR LIBRARY
from math import sqrt
# ENTRADA

lista = [10,33,9,14,18,114,12,21,50,55,60]
multiplosDeTres = []
raizCuadrada = []
# PROCESAMIENTO

for i in range(len(lista)):
     # calcular si modulo = 0 calcular la raiz cuadrada e imprimir resultado
    if lista[i] % 3 == 0:
        multiplosDeTres.append(lista[i])
        raizCuadrada.append(round(sqrt(lista[i]), 3))

# SALIDA
print('De la lista:', lista,'los multiples de 3 son:',multiplosDeTres,'y la raiz cuadrada de estos elementos es:',raizCuadrada)



###################### Ejercicio 2 ##############################
'''
Construya un programa en Python que simule el sorteo de
un juego de azar como el LOTO o el KINO
'''

#IMPORTAR LIBRARY
from random import sample
# ENTRADA
# Genera  de numeros
listaLoto = sorted(sample(range(1,41),6))
listaKino = sorted(sample(range(1,25),14))
#numeros jugados
numerosLoto = sorted(sample(range(1,41),6))
numerosKino = sorted(sample(range(1,25),14))

# PROCESAMIENTO
aciertosLoto = 0
for i in range(len(numerosLoto)):
    if numerosLoto[i] in listaLoto:
        aciertosLoto +=1

aciertosKino = 0
for i in range(len(numerosKino)):
    if numerosKino[i] in listaKino:
        aciertosKino +=1

# SALIDA
print('Juego Loto')
print('Dado los numeros del sorteo de Loto: ',listaLoto, 'Se jugaron los siguientes numeros',numerosLoto, 'Obteniendo',aciertosLoto,'aciertos' )

print('Juego Kino')
print('Dado los numeros del sorteo de Kino: ',listaKino, 'Se jugaron los siguientes numeros',numerosKino, 'Obteniendo',aciertosKino,'aciertos' )



###################### Ejercicio 3 ##############################
'''
Construya un programa en Python que reciba como
entrada un conjunto de valores, separados por el carácter
espacio y entregue como resultado el promedio y la
desviación estándar de dichos valores
'''

# ENTRADA
# solicitar datos
informacion = input('Ingrese los datos separados por espacio [Ejemplo: 1 2 3 4]\n')

# obtener informacion separada por " "
notas = []
for i in [n for n in informacion.split(" ")]:
    notas.append(float(i))

# PROCESAMIENTO

#funcion promedio valores
def promedio(numeros):
    promedio = sum(numeros) / len(numeros)
    return round(promedio,2)

#funcion desviacion estandar
def desvEst(numeros):
    numero = [float(i) for i in numeros]
    media = promedio(numeros)
    desviacion=0
    for i in range(0,len(numeros)):
        dif = ((numero[i] - media)**2)/ len(numeros) 
        desviacion=dif+desviacion
    return desviacion

# SALIDA     
print("los datos ingresados son:", notas)
print("El promedio para los datos ingresados es:", promedio(notas))
print("La desviacion estandar para los datos ingresados es:", desvEst(notas))