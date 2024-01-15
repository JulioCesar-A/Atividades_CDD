#dizer se o número é positivo ou negativo
continuar = "s"
while continuar == "s" or continuar == "S":
    num = int(input("Digite um número inteiro: "))
    while num == 0:
        num = int(input("Número inválido, digite outro número: "))
    if num < 0:
        print(f"O número digitado é negativo")
    else:
        print(f"O número digitado é positivo")
    continuar = input("Deseja continuar? ")