#receber o numeros de eleitores, separar os votos em brancos, nulos e válidos
#calcular o percentual de cada um em relação ao total
repetir = "s"
while repetir == "s" or repetir == "S":
    eleitores = int(input("Informe o número total de eleitores: "))
    contElei = 0
    nulos = 0
    brancos = 0
    validos = 0
    while contElei < eleitores:
        voto = input("Informe seu voto: ")
        if voto == "0" or voto =="00" or voto == "000" or voto == "0000":
            nulos += 1
            contElei += 1
        else:
            if voto == "branco" or voto == "Branco" or voto == "":
                brancos += 1
                contElei += 1
            else:
                validos += 1
                contElei += 1
    percB = brancos / eleitores * 100
    percV = validos / eleitores * 100
    percN = nulos / eleitores * 100
    print(f"Número de eleitores: {eleitores}\nVotos validados: {validos}\nVotos nulos: {nulos}\nVotos em branco: {brancos}")
    print(f"Percentual de votos\nNulos: {percN}%\nBrancos: {percB}%\nVálidos: {percV}%")
    repetir = input("Deseja refazer o cálculo? ")