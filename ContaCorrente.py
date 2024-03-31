class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def numeroContaGet(self):
        return self.numeroConta

    def numeroContaSet(self, numeroConta):
        self.numeroConta = numeroConta

    def nomeCorrentistaGet(self):
        return self.nomeCorrentista

    def nomeCorrentistaSet(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def saldoGet(self):
        return self.saldo

    def saldoSet(self, saldo):
        self.saldo = saldo

    def alteraNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor
        print("O depósito foi realizado!")
        print("Valor ainda em conta é de: " + str(self.saldo))

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("O saque foi realizado!")
            print("Valor sacado foi de: " + str(valor))
        else:
            print("O saque não pode ser realizado, saldo insuficiente!")

    def passagemDeDados(self):
        print("Nome do correntista: " , self.nomeCorrentista)
        print("Número da conta: " , self.numeroConta)
        print("Saldo atual da conta: R$" , str(self.saldo))

