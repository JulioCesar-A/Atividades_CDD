#tabuada
num = int(input("Digite um número inteiro: "))
print(f"A tabuada do número {num} é:")
for i in range (0,11,1):
    print(f"{num} * {i} = {num*i}")