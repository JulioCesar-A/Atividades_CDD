from Biblioteca import *
#do arquivo Biblioteca importar tudo(*)
repetir = "s"
while repetir == "s":
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    menu = input("Qual operação você deseja realizar? (1. Adição | 2. Subtração | 3. Multiplicação | 4. Divisão): ")
    while True:
        if menu == "1":
            somar(num1,num2)
            repetir = input("Deseja repetir o processo? ")
        elif menu == "2":
            subt(num1,num2)
            repetir = input("Deseja repetir o processo? ")
        elif menu == "3":
            mult(num1,num2)
            repetir = input("Deseja repetir o processo? ")
        elif menu == "4":
            div(num1,num2)
            repetir = input("Deseja repetir o processo? ")
        else:
            menu = input("Operação inválida, selecione as seguintes opções: (1. Adição | 2. Subtração | 3. Multiplicação | 4. Divisão): ")