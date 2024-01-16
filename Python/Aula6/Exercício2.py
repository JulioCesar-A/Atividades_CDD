I = []
cont = 0
numeros = 0

while cont < 9:
    if numeros % 2 == 0:
        numeros += 1
        I.append(numeros)
    else:
        numeros += 2
        I.append(numeros)
        cont += 1
print(I)