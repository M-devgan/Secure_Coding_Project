"""
Description: Unit tests for the Client class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_client.py
"""
# tests/test_client.py

import unittest
from client.client import Customer

class TestCustomer(unittest.TestCase):
    def test_init_valid_data(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(cust._cust_id, 1010)
        self.assertEqual(cust._fname, "Susan")
        self.assertEqual(cust._lname, "Clark")
        self.assertEqual(cust._email, "susanclark@pixell.com")

    def test_init_invalid_cust_id(self):
        with self.assertRaises(ValueError) as context:
            Customer("1010", "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(str(context.exception), "Customer ID must be integer.")

    def test_init_blank_fname(self):
        with self.assertRaises(ValueError) as context:
            Customer(1010, "", "Clark", "susanclark@pixell.com")
        self.assertEqual(str(context.exception), "First name can't be empty.")

    def test_init_blank_fname_spaces(self):
        with self.assertRaises(ValueError) as context:
            Customer(1010, "   ", "Clark", "susanclark@pixell.com")
        self.assertEqual(str(context.exception), "First name can't be empty.")

    def test_init_blank_lname(self):
        with self.assertRaises(ValueError) as context:
            Customer(1010, "Susan", "", "susanclark@pixell.com")
        self.assertEqual(str(context.exception), "Last name can't be empty.")

    def test_init_blank_lname_spaces(self):
        with self.assertRaises(ValueError) as context:
            Customer(1010, "Susan", "   ", "susanclark@pixell.com")
        self.assertEqual(str(context.exception), "Last name can't be empty.")

    def test_init_invalid_email(self):
        cust = Customer(1010, "Susan", "Clark", "invalid-email")
        self.assertEqual(cust._email, "email@pixell-river.com")

    def test_init_strips_names(self):
        cust = Customer(1010, "  Susan  ", "  Clark  ", "susanclark@pixell.com")
        self.assertEqual(cust._fname, "Susan")
        self.assertEqual(cust._lname, "Clark")

    def test_cust_id_property(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(cust.cust_id, 1010)

    def test_fname_property(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(cust.fname, "Susan")

    def test_lname_property(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(cust.lname, "Clark")

    def test_email_property(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        self.assertEqual(cust.email, "susanclark@pixell.com")

    def test_str_method(self):
        cust = Customer(1010, "Susan", "Clark", "susanclark@pixell.com")
        expected = "Clark, Susan [1010] - susanclark@pixell.com\n"
        self.assertEqual(str(cust), expected)

if __name__ == '__main__':
    unittest.main()