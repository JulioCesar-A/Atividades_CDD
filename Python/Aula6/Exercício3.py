A = [0,0,0,0,0,0,0,0,0,0]
for n in range(10):
    A[n] = int(input("Digite um número: "))
    
for p in range(10):
     if A[p] % 2 != 0: 
         print(A[p], "é ímpar")
for p in range(10): 
     if A[p] % 2 == 0: 
         print(A[p], "é par") 
for p in range(10): 
     if A[p] >= 0: 
         print(A[p], "é positivo")  
for p in range(10): 
     if A[p]< 0: 
         print(A[p], "é negativo") 
for p in range(10): 
     if A[p] == 0: 
         print(A[p])