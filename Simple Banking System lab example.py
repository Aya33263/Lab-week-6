#Simple Banking System lab example
#Step 1: Define the classes 
#first,for account
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount #add money "deposited"
        print(f"${amount} deposited .New balance :${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance :
            print ("Insufficient funds!")
        else:
            self.balance -= amount #money will less "withdrawn"
        print(f"${amount} withdrawn . New balance :{self.balance}")
    def display_balance(self):
       print(f"$ Account {self.account_number} balance :${self.balance}")

#second, for customer
class Customer :
    def __init__(self, name, account):
        self.name = name
        self.account = account
    def display_customer_info (self):
        print(f"customer Name: {self.name}")
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

# Step 2: Test the functionality 
# Creating an account and customer 
account1 = Account(account_number=101, balance=100)
customer1 = Customer(name ="Alice", account=account1)

# Display initial info 
customer1.display_customer_info()

# Performing transactions 
transaction1 = Transaction(account1, 50, "deposit")   #  50 deposit
transaction2 = Transaction(account1, 30, "withdraw")  #  30 withdraw

# Final account balance 
print("--- Final Status ---")
customer1.display_customer_info()