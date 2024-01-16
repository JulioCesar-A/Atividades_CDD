#Maçãs custo
quant = int(input("Quantas maçãs foram compradas? "))

if quant < 12:
    custo = quant * 1.30
    print(f"As maçãs custam: R${custo}")
else:
    custo = quant * 1
    print(f"As maçãs custam: R${custo}")
