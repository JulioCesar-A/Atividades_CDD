#Contagem de números
contnegat = 0
contposit = 10
somanegat = 0
somaposit = 0
for x in range (1,11,1):
    num = int(input("Digite um valor: "))
    if num < 0:
        contnegat += 1
        print(f"{num} é um número negativo")
        somanegat += num
        contposit = 10 - contnegat
print(f"Tem um total de {contnegat} número(s) negativo(s) e {contposit} número(s) positivo(s)")
print(f"O somatório dos números negativos é: {somanegat}")
