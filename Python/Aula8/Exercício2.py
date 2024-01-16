from Biblioteca import *
#do arquivo Biblioteca importar tudo(*)
repetir = "s"
while repetir == "s":
    menu = input("Qual operação você deseja realizar? (1. Adição | 2. Subtração | 3. Multiplicação | 4. Divisão): ")
    while True:
        if menu == "1":
            menu = int(input("Quantos valores você deseja somar? "))
            if menu == 2:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
                somar(num1, num2)
            elif menu == 3:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
                num3 = float(input("Digite o segundo valor: "))
                somar3(num1, num2, num3)
        elif menu == "2":
            subt(num1,num2)
        elif menu == "3":
            mult(num1,num2)
        elif menu == "4":
            div(num1,num2)
        else:
            menu = input("Operação inválida, selecione as seguintes opções: (1. Adição | 2. Subtração | 3. Multiplicação | 4. Divisão): ")