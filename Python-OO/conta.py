class Conta:
    def __init__(self, numero: str, titular, saldo: float, limite: float) -> None:
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_para_saque):
        valor_disponivel = self.saldo + self.limite
        return valor_disponivel <= valor_para_saque

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def tranfere(self, valor, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.limite += limite
    
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigo_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}