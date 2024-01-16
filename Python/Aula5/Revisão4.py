#maior entre 3 números
repetir = "s"
while repetir == "s" or repetir == "S":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    if num1 > num2:
        if num1 > num3:
            print(f"O primeiro número {num1} é o maior")
        else:
            print(f"O número {num3} é o maior")
    else:
        if num2 > num3:
            print(f"O número {num2} é o maior")
        else:
            print(f"O número {num3} é o maior")
    repetir = input("Deseja repetir o processo? ")