# combustivel
combustivel = input("Diga o tipo de combustível usado para abastecer (E-Etanol, G-Gasolina): ")
litrosvendidos = float(input("Indique a quantidade de litros abastecidos: "))
Total = 0
if combustivel == "G" or combustivel == "g":
    Total = 5.80 * litrosvendidos
    print(f"Total a pagar: R$ {Total}")
else:
    if combustivel == "E" or combustivel == "e":
        Total = 4.90 * litrosvendidos
        print(f"Total a pagar: R$ {Total}")
    else:
        print(f"Tipo de combustível inválido, por favor selecione uma das opcões previamente estabelecidas")

