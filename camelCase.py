frase="holaMundoComoEstasJuanCinco"
i=0 
total=1
while i < len(frase):
    if (frase[i].isupper()):
        total=total+1
    i=i+1
print("La cantidad de palabras es: ", total)