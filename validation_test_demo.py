import unittest
from creditCardValidation import *

class CreditCardValidationTest(unittest.TestCase):

    def setUp(self):
        print('Setup')

    def test_validateCard_valid(self):
        result = validateCard(date(2022, 2, 2))
        self.assertEqual('Valid', result)

    def test_validateCard_expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2020, 2, 2))

    def tearDown(self):
        print('tearDown')


if __name__ == '__main__':
    unittest.main()