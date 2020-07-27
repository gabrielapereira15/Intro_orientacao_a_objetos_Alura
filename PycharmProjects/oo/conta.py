class Conta:
    
    def __init__(self, numero, titular, saldo, limite): # __init__(self) inicia a construção de um objeto, def é para definir um método
        print("Construindo objeto...{}".format(self))
        self.__numero = numero # colocar __ antes dos atributos, encapsula o atributo, indicando que ele é um atributo que não deve ser alterado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def imprimir_extrato(self):
        print("Saldo: {}  Titular: {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if (self.__saldo_disponivel(valor)):
            self.__saldo -= valor
            print("Transação efetuada!")
        else:
            print("Saldo insuficiente!")

    def transferir(self, valor, destino):
        if (self.__saldo_disponivel(valor)):
            self.sacar(valor)
            destino.depositar(valor)
        else:
            print("Saldo insuficiente!")

    @property # define a propriedade do método, melhora a legibilidade e facilita o acesso, não precisa de ().
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title() # title() deixa o nome com a primeira letra maiúscula

    @property
    def limite(self):
        return self.__limite

    @limite.setter # setter indica que há a possibilidade de alterar um atributo privado através desse método
    def limite(self, limite):
        self.__limite = limite

    def __saldo_disponivel(self, valor):
        return valor <= self.__saldo + self.__limite

    @staticmethod # indica que é um método da Classe, n tem necessidade de ter um objeto
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
