#receber um número e mostrar seu antecessor e sucessor
repetir = "s"
while repetir == "s" or repetir == "S":
    num = int(input("Digite um número: "))
    ante = num - 1
    suce = num + 1
    menu = input("O que você quer? (1 - antecessor | 2 - sucessor) ")
    while menu == "1" or menu == "2":
        if menu == "1":
            print(f"O antecessor de {num} é: {ante}")
        else:
            if menu == "2":
                print(f"O sucessor de {num} é: {suce}")
        menu = input("Deseja alguma outra opção? (1 - antecessor | 2 - Sucessor | 3 - Encerrar) ")
    else:
        if menu == "3":
            print("Processo encerrado")
        repetir = input("Deseja refazer o processo com outro número? ")
print("Até breve")