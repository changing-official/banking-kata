import unittest
from account import Account

class TestBankingKata(unittest.TestCase):

    def testAccountExists(self):
        self.assertIsNotNone(Account())

    def testAccountDepositAcceptsValue(self):
        self.assertTrue(Account().deposit(100))

    def testAccountDepositDontAcceptString(self):
        with self.assertRaises(ValueError) as cm:
            Account().deposit("100aa")
        
        self.assertEqual(str(cm.exception), "Valor deve ser numérico")

    def testAccountDepositDontAcceptNegative(self):
        with self.assertRaises(ValueError) as cm:
            self.assertFalse(Account().deposit(-9))

        self.assertEqual(str(cm.exception), "Valor deve ser positivo")

    def testAccountDepositShowsMoney(self):
        conta = Account()
        conta.deposit(100)
        self.assertEqual(conta.money, 100)
        conta.deposit(200)
        self.assertEqual(conta.money, 300)

if __name__ == '__main__':
    unittest.main()