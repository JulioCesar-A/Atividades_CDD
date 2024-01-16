#Area retangulo
repetir = "s"
while repetir == "s" or repetir == "S":
    altura = float(input("Informe a altura do retângulo: "))
    while altura <= 0:
        altura = float(input("Número inválido, informe corretamente a altura do retângulo: "))
    base = float(input("Informe o comprimento da base do retângulo: "))
    while base <= 0:
        base = float(input("Número inválido, informe corretamente o comprimento da base do retângulo: "))
    area = base * altura
    print(f"A área desse retângulo: {area}")
    repetir = input("Deseja refazer o cálculo? ")