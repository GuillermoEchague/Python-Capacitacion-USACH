################ EJERCICIO 1 ###############################
''' Crear un programa para ordenar una lista, sin usar
métodos ni funciones de ordenamiento y sin calcular
mínimos ni máximos'''

print("Ornenador de listas de numeros, menos a mayor")
#Entrada
lista = [10,8,9,7,3,5,4,6,2,1,0]
print("Lista a ordenar: ", lista)
#Procesamiento
largoLista= len(lista)
while largoLista > 0 :
    largoLista = largoLista - 1
    indiceLista = 0
    while indiceLista < largoLista :
        if lista[indiceLista] > lista[indiceLista+1]:
            valorIndice = lista[indiceLista]
            lista[indiceLista] = lista[indiceLista+1]
            lista[indiceLista+1] = valorIndice
        indiceLista = indiceLista + 1 
#Salida
print("Los numeros ordenados son: ", lista)


################ EJERCICIO 2 ###############################
''''
Ejercicio listas 2a -  Encontrar numeros reperidos sin funciones ni metodos
Construya dos programas que encuentren el elemento que
más se repite en una lista:
Construya el primer programa sin usar los métodos . count (), sort () y index ()
'''

#Entrada
lista = [2,4,2,6,2,4,3,4]
#Procesamiento
i = 0
contadorFinal = 0
valorFinal = 0
while i < len(lista):
    valor = lista[i]
    i += 1
    j = 0
    contador = 0
    
    while j < len(lista):
        if valor == lista[j]:
            contador = contador + 1
        j = j + 1
    if contadorFinal < contador:
        contadorFinal = contador
        valorFinal = valor
#Salida
print("El valor que se repite mas veces es: ", valorFinal, " repetido ", contadorFinal, " veces ")


'''
Ejercicio listas 2b -  Encontrar numeros reperidos sin limitaciones de funciones y metodos
Como los métodos count (), sort () y index ()  
'''
#Entrada
lista = [2,4,2,6,2,4,3,4]
i = 0
listaAcumulador = []
contadorFinal = 0
valorFinal = 0
#Procesamiento
while i < len(lista):
    contador = lista.count(lista[i])
    listaAcumulador.append(contador)
    contadorFinal = max(listaAcumulador)
    valorFinal = lista[listaAcumulador.index(contadorFinal)]
    i += 1
#Salida
print("El numero con mas apariciones es: ", valorFinal, " con ", contadorFinal, " apariciones")

################  Ejercicio strings 1 ################  
'''
Construya un programa que solicite como entrada una
serie de números, separados por espacios y entregue
como salida un string con el cuadrado de cada número
separado por coma

'''
#Entrada
Entrada = "1 2 3 4"
print("Lista de entrada: ", Entrada)
#Procesamiento
lista = Entrada.split(' ')
i = 0
while i < len(lista):
    lista[i] = str(int(lista[i]) **2)
    i += 1
#Salida    
print("Lista de salida: ",", ".join(lista))

################  Ejercicio strings 2 ################  
'''
Entregar el promedio de notas del alumno junto con mensaje
explicativo para las entradas de tipo:
'Juan Perez 1 9;4.5,4.5,4.5,4.5'

Como mensaje de salida debe tener la siguiente forma:
'El alumno Juan Perez cedula de identidad nacional 1 9, tiene un
promedio de 4.5'
'''

#Entrada
alumno = 'Juan Perez;1-9;4.5,4.5,4.5,4.5'
alumno = alumno.split(";")
notas = alumno[2].split(",")
print('Datos del alumno:',alumno)
print('Notas del alumno:',notas)

#PROCESAMIENTO
largo =len(notas)
i = 0
suma = 0

while i < largo:
    notas[i] = float(notas[i])
    suma = suma + notas[i]
    i = i + 1
promedio = suma/i

#SALIDA
print('El alumno', alumno[0], 'cedula de identidad nacional', alumno[1],', tiene un promedio de', promedio)