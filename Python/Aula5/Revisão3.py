#dizer o ano em que a pessoa nasceu pela idade
idade = int(input("Digite sua idade? "))
mesNasc = int(input("Digite o mês em que nasceu: "))
mesAtual = 9
if mesNasc >= mesAtual:
    anoNasc = 2023 - idade - 1
else:
    anoNasc = 2023 - idade
print(anoNasc)
'''idade = int(input("Digite sua idade? "))
mesNasc = int(input("Digite o mês em que nasceu: "))
mesAtual = 9
anoNasc = 2023 - idade
if mesNasc >= mesAtual:
    anoNasc -=1
print(anoNasc)'''
