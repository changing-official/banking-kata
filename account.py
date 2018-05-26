class Account():

    _money = 0

    def deposit(self, value):
        
        convertido = 0

        try:
            convertido = float(value)
        except:
            raise ValueError("Valor deve ser numerico")

        if (convertido < 0 ):
           raise ValueError("Valor deve ser positivo")

        self._money += convertido

        return True

    def withdraw(self, value):

        if (value == 0):
            raise ValueError("Saque deve ser maior que zero")
        if (value > self._money):
            raise ValueError("Saldo Insuficiente")
        
        self._money -= value

    def printStatement(self):

        return self._money
