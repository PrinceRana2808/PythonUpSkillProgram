#Write a Python class named BankAccount with attributes like account_number, balance, and 
# customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}Rs deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount}Rs withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: {self.balance}Rs")


account1 = BankAccount("1234567890", "Prince Rana", 1000)
account1.deposit(500)
account1.withdraw(300)
account1.check_balance()