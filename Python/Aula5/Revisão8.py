#receber x números, calcular soma e média
quant = int(input("Digite quantos números você quer usar: "))
soma = 0
for x in range (quant):
    num = float(input("Digite um número: "))
    soma += num
media = soma / quant
print(f"A soma desses números é: {soma}\nA média desses números é: {media}")