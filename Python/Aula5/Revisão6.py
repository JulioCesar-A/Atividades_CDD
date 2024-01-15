#Ler numero diferente de 10, dizer se é maior ou menor
repetir = "s"
while repetir == "s" or repetir == "S":
    num = int(input("Digite um número: "))
    while num == 0:
      num = int(input("Número inválido por ser igual a 10. Digite um novo número: "))
    if num > 10:
        print("O número digitado é maior que 10")
    else:
        print("O número digitado é maior que 10")
    repetir = input("Deseja refazer o cálculo? ")