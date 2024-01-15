notas = [0,0,0,0,0]
#lista com 5 elementos
soma = 0
for j in range (5):
    notas[j] = float(input(f"Informe a nota №{j+1}: "))
#a variável j indica a posição dentro da lista (índice), 0 a 4
#o valor inserido será depositado na posição indicada por j
for t in range (5):
    soma += notas[t]
media = soma/5
for l in range (5):
    if notas[l] >= media:
        print(notas[l])
