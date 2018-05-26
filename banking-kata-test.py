import unittest
from account import Account

class TestBankingKata(unittest.TestCase):

    def testAccountExists(self):
        self.assertIsNotNone(Account())

    def testAccountDepositAcceptsValue(self):
        self.assertTrue(Account().deposit(100))

    def testAccountDepositDontAcceptInvalidValue(self):
        self.assertFalse(Account().deposit("100aa"))
        
        self.assertFalse(Account().deposit(-9))

    def testAccountDepositShowsMoney(self):
        conta = Account()
        conta.deposit(100)
        self.assertEqual(conta.money, 100)
        conta.deposit(200)
        self.assertEqual(conta.money, 300)

if __name__ == '__main__':
    unittest.main()