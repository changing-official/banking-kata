class Account():

    money = 0

    def deposit(self, value):
        try:
            convertido = float(value)

            if(convertido < 0 ):
                return False

            self.money += convertido
        except:
            return False

        return True