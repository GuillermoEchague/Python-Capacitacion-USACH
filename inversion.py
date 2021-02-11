''' 
Escribir un programa que calcule el resultado de una inversión con interés
compuesto preguntado al usuario el capital, el interés anual y la cantidad de
periodos (en años), y muestre por pantalla el resultado obtenido.
'''
print('Programa para determinar el resultado de una inversión agregando capital inicial, interes y tiempo en años')
print('Por favor ingrese lo siguiente: ')

#DATOS DE ENTRADA

# Capital inicial
c=int(input('Ingrese capital inicial:'))

# Interes
r=float(input('Ingrese interes anual:'))

# Tiempo en años
t=int(input('Ingrese cantidad de años:'))

#PROCESAMIENTO
# Interes compuesto
C_F=c*(1+r/100)**t


#SALIDAS
# Resultado del
print('El valor total es: ',C_F)