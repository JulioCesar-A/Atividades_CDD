# numeros em ordem crescente
print("Vamos ordenar os números")
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
if num1 == num2:
    print(f"Os números são iguais: {num1} não é diferente de {num2}")
else:
    if num1 < num2:
        print(f"Em ordem crescente: {num1, num2}")
    else:
        print(f"Em ordem crescente: {num2,num1}")
