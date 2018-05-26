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
        raise ValueError("Saldo Insuficiente")
    
    def printStatement(self):
        return self._money
        