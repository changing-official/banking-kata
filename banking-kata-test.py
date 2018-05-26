import unittest
from account import Account

class TestBankingKata(unittest.TestCase):

    def testAccountExists(self):
        self.assertIsNotNone(Account)

if __name__ == '__main__':
    unittest.main()