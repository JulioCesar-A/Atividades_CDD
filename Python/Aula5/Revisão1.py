#duas notas e media
repetir = "s"
while repetir == "s" or repetir == "S":
    nota1 = float(input("Digite a nota da primeira avaliação: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Nota inválida, digite novamente: "))
    nota2 = float(input("Digite a nota da segunda avaliação: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Nota inválida, digite novamente: "))
    media = (nota1+nota2)/2
    print(f"A média desse aluno é: {media}")
    if media >= 7:
        print(f"Aprovado")
    else:
#pode trocar o else de cima e o if de baixo por um elif
        if media < 4:
            print(f"Reprovado")
        else:
            print(f"Em recuperação")
    repetir = input("Deseja refazer o cálculo? ")