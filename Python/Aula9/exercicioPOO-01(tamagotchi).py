from bibliotecaClasses import *

p1 = Pessoa("Ranna", 19,49)
print(p1.nome, p1.idade, p1.peso)
p1.comer("feijão")
p1.parar_comer()
p1.andar()
p1.parar_andar()
p1.dormir()
p1.acordar()

p2 = Pessoa("Marcelo", 26, 75)
print(p1.nome, p1.idade, p1.peso)
p2.comer("arroz")
p2.parar_comer()
p2.andar()
p2.parar_andar()
p2.dormir()
p2.acordar()