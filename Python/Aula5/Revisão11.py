#ler idade em anos, meses e dias e converter apenas em dias
repetir = "s"
while repetir == "s" or repetir == "S":
    idade = int(input("Digite sua idade (em anos): "))
    mesNasc = int(input("Digite o mês em que você nasceu: "))
    mesAtual = int(input("Digite o mês em que estamos: "))
    diaNasc = int(input("Digite o dia em que você nasceu: "))
    diaAtual = int(input("Digite o dia em que estamos: "))
    idadeDias = (365 * idade) + (mesAtual + mesNasc) * 30 + (diaAtual-diaNasc)
    print(f"Você viveu {idadeDias} dias, meus parabéns???")
    repetir = input("Deseja refazer o cálculo? ")
print("Até breve")