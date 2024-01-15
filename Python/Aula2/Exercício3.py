# partida futebol
time1 = input("Escreva o nome do time: ")
goltime1 = int(input("Escreva a quantidade de gols marcados pelo time 1: "))
time2 = input("Escreva o nome do outro time: ")
goltime2 = int(input("Escreva a quantidade de gols marcados pelo time 2: "))
if goltime1 < 0 or goltime2 < 0:
    print("Informações inválidas")
else:
    if goltime1 == goltime2:
        print(f"Partida encerrou em empate: \n{time1}: {goltime1} \n{time2}: {goltime2}")
    else:
        if goltime1 > goltime2:
            print(f"{time1} venceu a partida: \n{time1}: {goltime1} \n{time2}: {goltime2}")
        else:
            print(f"{time2} venceu a partida: \n{time1}: {goltime1} \n{time2}: {goltime2}")