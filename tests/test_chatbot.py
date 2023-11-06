"""
Description: In this code tests are being performed on the functions defined in the chatbot.py file to ensure smooth functionality. 
Author:Parneet 
Date:11/5/2023
Usage:this code will run tests simulating various situations the chatbot should face any issues. 
"""
import unittest
from unittest.mock import patch
from ..src.chatbot import get_account,VALID_TASKS, ACCOUNTS,get_account, get_amount

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
        # Act
        with patch("builtins.input", side_effect=["500.01"]):
            result = get_amount()
            # Assert
            self.assertEqual(result, 500.01)

      
         