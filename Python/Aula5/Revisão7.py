#area de um triângulo

repetir = "s"

while repetir == "s" or repetir == "S":
    altura = float(input("Informe a altura do triângulo: "))
    while altura <= 0:
        altura = float(input("Tamanho inválido, informe outro número: "))
    base = float(input("Informe o comprimento da base: "))
    while base <= 0:
        base = float(input("Tamanho inválido, informe outro número: "))
    area =(base*altura)/2
    print(f"A área desse triângulo é: {area}")
    repetir = input("Deseja refazer o cálculo? ")