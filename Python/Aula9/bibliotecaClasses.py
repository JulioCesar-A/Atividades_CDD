class ContaBancaria:
    def __init__(self, n, num, t):
        self.NomeCliente = n
        self.NumeroConta = num
        self.TipoConta = t
        self.Limite = 0
        self.LimiteAux = 0
        self.Saldo = 0
        self.StatusConta = False

    def AtivarConta(self):
        if self.StatusConta == True:
            print(f"Sua conta já está ativada")
        else:
            if self.StatusConta == False:
                print("Sua conta será ativada, por favor aguarde")
                self.StatusConta = True
                print(f"Status atual da conta: Ativa")

    def DesativarConta(self):
        if self.StatusConta == False:
            print(f"Sua conta já está desativada")
        else:
            if self.Saldo > 0:
                print(f"Por favor, retire o dinheiro da sua conta antes de desativá-la\nSaldo Atual: R${self.Saldo}")
            else:
                if self.Saldo < 0:
                    print(f"Para desativar sua conta, você deve resolver os seus débitos\nSaldo Atual: R${self.Saldo}")
                else:
                    print(f"Sua conta será desativada, por favor aguarde")
                    self.StatusConta = False
                    print(f"Status atual da conta: Inativa")

    def Sacar(self, valorSaq):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            if self.Limite > 0:
                if valorSaq > self.Saldo:
                    if valorSaq < self.Limite + self.Saldo:
                        self.Saldo += self.Limite
                        self.LimiteAux = self.Limite
                        self.Limite = self.Saldo - valorSaq
                        print(f"Limite atual: R${self.Limite}")
                        if self.Saldo <= 0 or self.Saldo < valorSaq:
                            print(f"Saldo insuficiente.\nSaldo Disponível: R${self.Saldo}")
                        else:
                            self.Saldo -= valorSaq
                            print(f"Valor sacado: R${valorSaq}\nSaldo atual: R${self.Saldo}")
                    else:
                        self.Saldo += self.Limite
                        print(f"ei nêga, tá querendo gastar o que não tem???????\nSaldo atual: R${self.Saldo}")
            else:
                if self.Saldo <= 0 or self.Saldo < valorSaq:
                    print(f"Saldo insuficiente.\nSaldo Disponível: R${self.Saldo}")
                else:
                    self.Saldo -= valorSaq
                    print(f"Valor sacado: R${valorSaq}\nSaldo atual: R${self.Saldo}")

    def Depositar(self, valorDep):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            if self.Limite < self.LimiteAux:
                print(f"Valor depositado: R${valorDep}")
                self.Limite += (self.LimiteAux - self.Saldo)
                print(f"Valor direcionado ao limite de crédito: R${self.LimiteAux - self.Saldo}")
                self.Saldo += (self.LimiteAux - valorDep)
                print(f"Saldo atual: R${self.Saldo}")
            else:
                self.Saldo += valorDep
                print(f"Valor depositado: R${valorDep}")

    def VerificarSaldo(self):
        if self.StatusConta == False:
            print(f"Operação inválida (Status atual da conta: Inativa). Primeiro ative a conta")
        else:
            print(f"Saldo atual: R${self.Saldo}")
    def InfoConta(self):
        print(f"Nome do Cliente: {self.NomeCliente}\nNúmero da conta: {self.NumeroConta}\nTipo da conta: {self.TipoConta}")

    def LimiteConta(self, valorLim):
        self.Limite = valorLim
        print(f"Valor do limite: R${valorLim}")



class Pessoa:

    def __init__(self, n, i, p, c=False, d=False, a=False):
        self.nome = n
        self.idade = i
        self.peso = p
        self.comendo = c
        self.dormindo = d
        self.andando = a

    def andar(self):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.andando = True
            print(f"{self.nome} foi andar. . .")
        elif self.andando == True:
            print(f"{self.nome} ainda está andando")

    def parar_andar(self):
        if self.andando == True:
            self.andando = False
            print(f"{self.nome} terminou de andar.")
        else:
            print(f"{self.nome} não está andando.")

    def comer(self, comida):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.comida = comida
            self.comendo = True
            print(f"{self.nome} foi comer {self.comida}")
        elif self.comendo == True:
            print(f"Termine sua comida antes de comer novamente.")

    def parar_comer(self):
        if self.comendo == True:
            self.comendo = False
            print(f"{self.nome} terminou de comer.")
        else:
            print(f"{self.nome} não está comendo.")

    def dormir(self):
        if self.andando == False and self.comendo == False and self.dormindo == False:
            self.dormindo = True
            print(f"{self.nome} foi dormir. . .")
        elif self.dormindo == True:
            print(f"{self.nome} já está dormindo")

    def acordar(self):
        if self.dormindo == True:
            self.dormindo = False
            print(f"{self.nome} acordou.")
        else:
            print(f"{self.nome} não está dormindo.")

class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"{self.nome} foi miando...")