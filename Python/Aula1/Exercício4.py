# dados_pessoa
nome = input("Informe seu nome e sobrenome: ")
idade = int(input("Informe sua idade: "))
filhos = int(input("Informe o número de filhos: "))
abono = filhos*150
salario = float(input("Informe seu salário (em R$): "))
taxa = float(input("Informe a taxa de crescimento: "))/100
novosalario = salario+(salario*taxa)
ferias = novosalario/3
INSS = novosalario*8/100
ImRenda = novosalario*15/100
salario_resto = novosalario-ImRenda-INSS
print(f"Os dados informados: \nNome: {nome} Idade: {idade} \nSalário: R$ {salario}")
print(f"Salário reajustado para: R$ {novosalario}")
print(f"Abono família: R$ {abono} \nFérias: R$ {ferias}")
print(f"Descontos: \nINSS(8%): {INSS}\nImposto de Renda(15%): {ImRenda}")
print(f"Salário restante: {salario_resto}")
