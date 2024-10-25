"""
Requirements:

The program should have a predefined dictionary of users with their account
numbers and balances.
Users should be able to check their balance, deposit money, and withdraw money.
The program should ask for the user's account number and validate it.
If the account number is valid, the program should display a menu with options
to check balance, deposit money, and withdraw money.
For the deposit and withdrawal options, the program should ask for the amount
and update the balance accordingly.
The program should handle invalid inputs and display appropriate error messages.

Example of the predefined dictionary:

accounts = {
    '123456': {'name': 'John Doe', 'balance': 1500},
    '789012': {'name': 'Jane Smith', 'balance': 2000},
    '345678': {'name': 'Alice Johnson', 'balance': 500}
}

Proposed usage example:

Please enter your account ID:
# 2233
This account ID is not valid. Please enter your account ID:
# 123456
Hi John, your account balance is 1500 coins.
Use '+' to add coins, or '-' to withdraw coins. Use '?' to check your balance.
Type 'exit' to quit.
> +300
Deposited: +300 coins. New balance: 1800 coins
> -5000
Error: Insufficient balance
> ?
Balance: 1800 coins
> -500
Withdrew: -500 coins. New balance: 1300 coins
> exit

Thank you for using the ATM. Goodbye!
"""

# accounts = {
#     '123456': {'name': 'John Doe', 'balance': 1500},
#     '789012': {'name': 'Jane Smith', 'balance': 2000},
#     '345678': {'name': 'Alice Johnson', 'balance': 500}
# }
#
# def autorisation():
#     n = input("Enter your login please: ")
#
#     if n in accounts:  # как мне вывести имя и баланс который соответствует конкретмому номеру, если я изначально только смотрела есть ли номер в дикте, а не какой он именно.
#         person = accounts[n]
#         print(f'Hello, {person["name"]}, your account balance is {accounts[n]["balance"]}')
#         input("Use '+' to add coins, or '-' to withdraw coins. Use '?' to check your balance.Type 'exit' to quit.")
#     else:
#         input("This account ID is not valid. Please enter your account ID: ")  # это прировнять к еще одной переменной?


# autorisation()


ACCOUNTS = {
    '123456': {'name': 'John Doe', 'balance': 1500},
    '789012': {'name': 'Jane Smith', 'balance': 2000},
    '345678': {'name': 'Alice Johnson', 'balance': 500}
}


class Authorization:

    def __init__(self, accounts):
        self.accounts = accounts

    def validate_account(self, account_number):
        if account_number in self.accounts:
            return True
        return False




class Balance:

    def __init__(self, accounts):
        self.accounts = accounts

    def check_balance(self, account_number):
        return self.accounts[account_number]['balance']


    def deposit_money(self, account_number, money):
        self.accounts[account_number]['balance'] += money
        return self.accounts[account_number]['balance']


    def take_the_money(self, account_number, amount):
        if self.accounts[account_number]['balance'] < amount:
            raise ValueError(amount)
        self.accounts[account_number]['balance'] -= amount
        return self.accounts[account_number]['balance']


class ATM:

    def __init__(self):
        self.account_number = None


    def authenticate(self):
        while True:
            n = input('Please enter your account ID: ')
            if n not in ACCOUNTS:
                print('This account ID is not valid. ', end='')

            else:
                self.account_number = n
                break

    def acc_operations(self):
        pass

atm = ATM()
atm.authenticate()
