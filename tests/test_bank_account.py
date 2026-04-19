"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
# tests/test_bank_account.py

import unittest
from bank_account.bank_account import BankAcct

class TestBankAcct(unittest.TestCase):
    
    def test_init_valid_data(self):
        acct = BankAcct(20019, 1010, 1000.50)
        self.assertEqual(acct._acct_num, 20019)
        self.assertEqual(acct._cust_id, 1010)
        self.assertEqual(round(acct._bal, 2), 1000.50)
    
    def test_init_invalid_account_number(self):
        with self.assertRaises(ValueError) as context:
            BankAcct("20019", 1010, 1000.50)
        self.assertEqual(str(context.exception), "Account number must be integer.")
    
    def test_init_invalid_client_number(self):
        with self.assertRaises(ValueError) as context:
            BankAcct(20019, "1010", 1000.50)
        self.assertEqual(str(context.exception), "Customer ID must be integer.")
    
    def test_init_invalid_balance(self):
        acct = BankAcct(20019, 1010, "invalid")
        self.assertEqual(acct._bal, 0.0)
    
    def test_init_string_balance_convertible(self):
        acct = BankAcct(20019, 1010, "1000.50")
        self.assertEqual(round(acct._bal, 2), 1000.50)
    
    def test_acct_num_property(self):
        acct = BankAcct(20019, 1010, 1000.50)
        self.assertEqual(acct.acct_num, 20019)
    
    def test_cust_id_property(self):
        acct = BankAcct(20019, 1010, 1000.50)
        self.assertEqual(acct.cust_id, 1010)
    
    def test_bal_property(self):
        acct = BankAcct(20019, 1010, 1000.50)
        self.assertEqual(round(acct.bal, 2), 1000.50)
    
    def test_change_bal_valid(self):
        acct = BankAcct(20019, 1010, 1000.50)
        acct.change_bal(500.25)
        self.assertEqual(round(acct._bal, 2), 1500.75)
    
    def test_change_bal_negative(self):
        acct = BankAcct(20019, 1010, 1000.50)
        acct.change_bal(-200.25)
        self.assertEqual(round(acct._bal, 2), 800.25)
    
    def test_change_bal_invalid(self):
        acct = BankAcct(20019, 1010, 1000.50)
        original_balance = acct._bal
        acct.change_bal("invalid")
        self.assertEqual(acct._bal, original_balance)
    
    def test_add_funds_valid(self):
        acct = BankAcct(20019, 1010, 1000.50)
        acct.add_funds(500.25)
        self.assertEqual(round(acct._bal, 2), 1500.75)
    
    def test_add_funds_invalid_type(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.add_funds("invalid")
        self.assertEqual(str(context.exception), "Deposit must be numeric: invalid")
    
    def test_add_funds_negative_amount(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.add_funds(-100.00)
        self.assertEqual(str(context.exception), "Deposit must be positive: $-100.00")
    
    def test_add_funds_zero_amount(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.add_funds(0)
        self.assertEqual(str(context.exception), "Deposit must be positive: $0.00")
    
    def test_take_funds_valid(self):
        acct = BankAcct(20019, 1010, 1000.50)
        acct.take_funds(200.25)
        self.assertEqual(round(acct._bal, 2), 800.25)
    
    def test_take_funds_invalid_type(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.take_funds("invalid")
        self.assertEqual(str(context.exception), "Withdraw must be numeric: invalid")
    
    def test_take_funds_negative_amount(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.take_funds(-100.00)
        self.assertEqual(str(context.exception), "Withdraw must be positive: $-100.00")
    
    def test_take_funds_zero_amount(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.take_funds(0)
        self.assertEqual(str(context.exception), "Withdraw must be positive: $0.00")
    
    def test_take_funds_exceeds_balance(self):
        acct = BankAcct(20019, 1010, 1000.50)
        with self.assertRaises(ValueError) as context:
            acct.take_funds(1500.00)
        self.assertEqual(str(context.exception), "Withdraw $1,500.00 exceeds balance $1,000.50.")
    
    def test_str_method(self):
        acct = BankAcct(20019, 1010, 6764.67)
        expected = "Acct#: 20019 Bal: $6,764.67\n"
        self.assertEqual(str(acct), expected)

if __name__ == '__main__':
    unittest.main()