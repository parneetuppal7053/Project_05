"""
Description: In this code tests are being performed on the functions defined in the chatbot.py file to ensure smooth functionality. 
Author:Parneet 
Date:11/5/2023
Usage:this code will run tests simulating various situations the chatbot should face any issues. 
"""
import unittest
from unittest.mock import patch
from ..src.chatbot import get_account,VALID_TASKS, ACCOUNTS,get_account, get_amount, get_balance,make_deposit

class ChatbotTests(unittest.TestCase):
    #TEST 01 
    def test_valid_account(self):
        """tests the user input by mocking it from the builtin patch files 
            getting the account number input from the user 
        """
        #ACT
        with patch("builtins.input")as mock_input: 
            mock_input.side_effect = ["123456"]
            account_number = get_account()
        #ASSERT
            self.assertEqual(account_number, 123456)
            
    #TEST 02 
    def test_non_numeric_input(self):
        """ tests the chatbot program for any non numeric input the user puts 
            return an error message in the form of a string  
        """
        #ACT
        with patch("builtins.input") as mock_input:
            mock_input.side_effect= ["non_numeric_data"]
            with self.assertRaises(ValueError) as context:
                get_account()
        # ASSERT
            self.assertEqual(str(context.exception), "Account number must be a whole number.")
    
    #TEST 03
    def test_account_not_in_accounts(self):
        """ tests the chatbot program for input and checks the accounts dictionary 
            if account does not exists it raises an exception  
            return an error message in the form of a string  
        """
        #ACT
        with patch("builtins.input") as mock_input: 
            mock_input.side_effect["112233"]
            with self.assertRaises(Exception) as context:
                get_account()
        #ASSERT
            self.assertEqual(str(context.exception), "Account number entered does not exist.")
            
    #TEST 04
    def test_get_amount_valid_amount(self):
        #act
        with patch("builtins.input")as mock_input:
            mock_input.side_effect= ["500.01"]
            result = get_amount()
        #assert
            self.assertEqual(result, 500.01)
    
    #TEST 05
    def test_get_non_numeric_input(self):
        #act
        with patch("builtins.input")as mock_input:
            mock_input.side_effect= ["non_numeric_data"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        #assert
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")  
    
    #TEST 06 
    def test_get_zero_or_negative(self):
        #act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["0"]
            with self.assertRaises(ValueError) as context:
                get_amount()
        #assert
            self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.") 
   
    #TEST 07
    def test_valid_account_get_balance(self):
        #act
        with patch("builtins.input")as mock_input:
            mock_input.side_effect = ["123456"]
            balance_data = get_balance(int(input("Enter account number: ")))
            expected_message = 'Your current balance for account 123456 is $1000.00.'
        #assert
            self.assertEqual(balance_data, expected_message)
    
    #TEST 08
    def test_account_not_in_accounts_get_balance(self):
        #act
        with patch("builtins.input") as mock_input:
            mock_input.side_effect=["112233"]
            with self.assertRaises(Exception) as context:
                get_balance(int(input("Enter account number: ")))
        #assert
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    #TEST 09    
    def test_updated_balance_make_deposit(self):
        
        #arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        deposit_amount = 1500.01
        
        #act
        make_deposit(account_number, deposit_amount)
        
        #assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)
    
    #TEST 10
    def test_make_deposit_successful_message(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0
        # Act
        result = make_deposit(account_number, 1500.01)
        # Assert
        self.assertEqual(result, "You have made a deposit of $1500.01 to account 123456.")

    #TEST 11
    def test_make_deposit_account_not_exist(self):
        # Arrange
        account_number = 112233
        deposit_amount = 1500.01
        # Act
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(str(context.exception), "Account number does not exist.")
    
    #TEST 12
    def test_make_deposit_negative_amount(self):
        # Arrange
        account_number = 123456
        deposit_amount = -50.01
        # Act
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, deposit_amount)
        # Assert
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.")
