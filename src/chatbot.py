"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Parneet}
Date: 2023-11-5
Usage: From the console: python src/chatbot.py
"""

# ## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

# VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:
def get_account():
 while True:
    try: 
        account_number = int ((input("Please enter your account number: ")))
        if account_number %1 !=0:
          raise ValueError("Account number must be a whole number.")
        if account_number in ACCOUNTS:
            return account_number
        else:
            raise Exception("Account number entered does not exist.")
    except ValueError : 
        print("Account number must be a whole number.") 
    except Exception as error:
        print(error)        


def get_amount() -> float:
    while True:
        try:
            # Prompt the user for input
            amount_input = input("Enter the transaction amount: ")
            try:
                amount = float(amount_input)
            except ValueError:
                raise ValueError("Invalid amount. Amount must be numeric.")
            if amount <= 0:
                raise ValueError("Invalid amount. Please enter a positive number.")

            return amount
        except ValueError as Flaw:
            raise(Flaw)


def get_balance(account: int) -> str:
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")
    balance = ACCOUNTS[account]["balance"]
    return f'Your current balance for account {account} is ${balance:.2f}.'

def make_deposit(account: int, deposit: float) -> str:
    """
    Args:
        account (int): The account number
        amount (float): The amount to deposit
    Returns:
        string: A message whenever there is a successful deposit
    Raises:
        Exception: If the account number does not exist in the "accounts" dictionary
        ValueError: If the amount is not greater than zero
    """
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")

    if deposit <= 0:
        raise ValueError("Invalid Amount. Amount must be positive.")

    ACCOUNTS[account]["balance"] += deposit

    return f"You have made a deposit of ${deposit:.2f} to account {account}."

def user_selection()-> str:
    """
    This function gets the input from the users from a range of options given
    Raises:
        ValueError: if the user inputs any other value rather than the (balance,deposit, or exit)
    Returns:
        str: the selected task from the list is returned in the form of string 
    """
    VALID_TASKS = ["balance", "deposit", "exit"]
    while True:
        task = input("What would you like to do (balance/deposit/exit)? ").lower()
        if task in VALID_TASKS:
            return task
        else:
            raise ValueError("Invalid task. Please choose balance, deposit, or exit.")

## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

def chatbot():
    
    # The main program.  Uses the functionality of the functions:
    #     get_account()
    #     get_amount()
    #     get_balance()
    #     make_deposit()
    #     user_selection()
    

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            selection = user_selection()
            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                       account = get_account()
                       valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                    BALANCE =get_balance(account)
                    print(BALANCE)

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            amount = get_amount()
                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    RESult_deposit = make_deposit(account,amount)
                    print(RESult_deposit)
            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
 

if __name__ == "__main__":
    chatbot()
                     


                           


            
  


            
    
