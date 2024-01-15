from bibliotecaClasses import *

conta1 = ContaBancaria("Lucas", "123456-78","Corrente")
conta1.InfoConta()

conta1.AtivarConta()
conta1.Depositar(100)
conta1.LimiteConta(1000)
conta1.Sacar(2000)