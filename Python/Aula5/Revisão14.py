#ler temperatura em uma escala e converter em outra
repetir = "s"

while repetir == "s" or repetir == "S":
    escala = input("Escolha uma escala (C ou F): ")
    if escala == "f" or escala == "F":
        F = float(input("Informe a temperatura em fahrenheit: "))
        C = ((F - 32)/9)*5
        print(f"Convertendo para graus Celsius: {C}")
    else:
        if escala == "c" or escala == "C":
            C = float(input("Informe a temperatura em celsius: "))
            F = (C*9/5)+32
            print(f"Convertendo para graus fahrenheit: {F}")
    repetir = input("Deseja refazer o cálculo? ")

print("Até breve")