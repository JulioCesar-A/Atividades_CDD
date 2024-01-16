# media aluno
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))
if (nota1 < 0) or (nota1 > 10) or (nota2 < 0) or (nota2 > 10) or (nota3 < 0) or (nota3 > 10):
    print(f"Alguma(s) nota(s) está inválida(s), corrija-a(s)")
else:
    media = (nota1+nota2+nota3)/3
    if media >= 7.0:
        print(f"Sua média é: {media} \nVocê está aprovado")
    else:
        if media < 4.0:
            print(f"Sua média é: {media} \nVocê está reprovado")
        else:
            print(f"Sua média é: {media} \nVocê foi para recuperação")
