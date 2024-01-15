#Duração de uma partida
DiaInic = int(input("Informe o dia de início da partida: "))
HoraInic = int(input("Informe o horário de início da partida: "))

while HoraInic < 0 or HoraInic > 23:
  HoraInic = int(input("Informe corretamente o horário de início da partida: "))
  
DiaFim = int(input("Informe o dia de término da partida: "))
HoraFim = int(input("Informe o horário de término da partida: "))

while HoraFim < 0 or HoraFim > 23:
  HoraFim = int(input("Informe corretamente o horário de término da partida: "))
  
if DiaInic == DiaFim:
  Duracao = HoraFim - HoraInic
  print(f"A partida durou {Duracao} hora(s)")
else:
  if DiaInic < DiaFim:
    Duracao = 24 + HoraFim - HoraInic
  if HoraFim > HoraInic:
    print(f"Partida excede o tempo limite (24 horas)")
print(f"A partida durou {Duracao} hora(s)")
