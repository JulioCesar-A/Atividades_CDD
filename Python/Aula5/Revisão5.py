#par ou impar
repetir = "s"
while repetir == "s" or repetir == "S":
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")
    repetir = input("Deseja refazer o cálculo? ")