#Step 1: Define the classes edit with input

#first,for account
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")
#second, for customer
class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def display_customer_info(self):
        print(f"\n--- Customer Name: {self.name} ---")
        self.account.display_balance()
#third,for transaction
class Transaction:
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()

    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")

# --- Step 2: Test with User Input 

print("\n=== Welcome to the Banking System ===\n")

# Take User Data 
name_input = input("Enter Customer Name: ")
account_input = input("Enter Account Number : ")
balance_input = float(input("Enter Starting Balance: "))

#  Create the Objects
user_account = Account(account_number=account_input, balance=balance_input)
user_customer = Customer(name=name_input, account = user_account )

#  Show Initial Status
user_customer.display_customer_info()

# Perform a Transaction based on user choice
transaction_type = input("Enter transaction type - deposit or withdraw : ").lower()
transaction_amount = float(input("Enter amount : "))

# Execute Transaction
Transaction( user_account, transaction_amount, transaction_type)

# Show Final Status
print("\n--- Final Status ---")
user_customer.display_customer_info()