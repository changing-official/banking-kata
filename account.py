class Account():

    money = 0

    def deposit(self, value):
        convertido = 0

        try:
            convertido = float(value)
        except:
            raise ValueError("Valor deve ser numérico")

        if (convertido < 0 ):
           raise ValueError("Valor deve ser positivo")

        self.money += convertido

        return True