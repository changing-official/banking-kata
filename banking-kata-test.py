
import unittest
from account import Account

class TestBankingKata(unittest.TestCase):

    @classmethod
    def setUp(self):
       self.conta = Account()

    def testAccountExists(self):
        self.assertIsNotNone(self.conta)

    def testAccountDepositAcceptsValue(self):
        self.assertTrue(self.conta.deposit(100))

    def testAccountDepositDontAcceptString(self):
        with self.assertRaises(ValueError) as cm:
            self.conta.deposit("100aa")
        
        self.assertEqual(str(cm.exception), "Valor deve ser numerico")

    def testAccountDepositDontAcceptNegative(self):
        with self.assertRaises(ValueError) as cm:
            self.assertFalse(self.conta.deposit(-9))

        self.assertEqual(str(cm.exception), "Valor deve ser positivo")

    def testAccountDepositShowsStatement(self):
        self.conta.deposit(100)
        self.assertEqual(self.conta.printStatement(), 100)
        self.conta.deposit(200)
        self.assertEqual(self.conta.printStatement(), 300)

    def testAccountPrintStatementWorks(self):
        self.assertEqual(self.conta.printStatement(), 0)

    def testAccountWithdrawRaisesErrorWhenZeroBalance(self):
        with self.assertRaises(ValueError) as cm:
            self.conta.withdraw(1)

        self.assertEqual(str(cm.exception), "Saldo Insuficiente")

    def testAccountWithdrawShouldBeGreaterThanZero(self):
        with self.assertRaises(ValueError) as cm:
            self.conta.withdraw(0)

        self.assertEqual(str(cm.exception), "Saque deve ser maior que zero")

    def testAccountWithdrawShouldWithdraw(self):
        
        self.conta.deposit(100)
        self.conta.withdraw(100)

        self.assertEqual(self.conta.printStatement(), 0)

if __name__ == '__main__':
    unittest.main()
    
