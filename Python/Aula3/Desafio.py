#Pedra, papel ou tesoura
VitJ1 = 0
VitJ2 = 0
while VitJ1 < 2 and VitJ2 < 2:
    JogadaJ1 = input("Jogador 1, faça sua jogada (Com inicial maiúscula): ")
    JogadaJ2 = input("Jogador 2, faça sua jogada (Com inicial maiúscula): ")
    if JogadaJ1 == JogadaJ2:
        print("Partida empatada")
    else:
        if (JogadaJ1 == "Papel" and JogadaJ2 == "Pedra") or (JogadaJ1 == "Pedra" and JogadaJ2 == "Tesoura") or (JogadaJ1 == "Tesoura" and JogadaJ2 == "Papel"):
            print("Jogador 1 ganhou a partida")
            VitJ1 += 1
        else:
            print("Jogador 2 ganhou a partida")
            VitJ2 += 1
if VitJ1 > VitJ2:
    print("Jogador 1 venceu o jogo")
else:
    print("Jogador 2 venceu o jogo")
