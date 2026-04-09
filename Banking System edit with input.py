#Step 1: Define the classes edit with input

#first,for account
class Account:
     # Initialize the account with a number and an optional starting balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        
    # Method to add money to the current balance
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    # Method to remove money if there are enough funds available
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")
     # Method to print the current account status
    def display_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance}")
        
# Define the Customer class to link a person to an Account object
class Customer:
    # Initialize the customer with a name and their specific Account object
    def __init__(self, name, account):
        self.name = name
        self.account = account
     # Method to show customer details by calling the Account's display method
    def display_customer_info(self):
        print(f"\n--- Customer Name: {self.name} ---")
        self.account.display_balance()
        
# Define the Transaction class to handle the logic of deposits or withdrawals
class Transaction:
    # Initialize and immediately trigger the processing of the transaction
    def __init__(self, account, amount, transaction_type):
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        self.process_transaction()
        
    # Determine whether to call the deposit or withdraw method based on input
    def process_transaction(self):
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")

# --- Step 2: Test with User Input 

print("\n=== Welcome to the Banking System ===\n")

# Capture user information from the console 
name_input = input("Enter Customer Name: ")
account_input = input("Enter Account Number : ")
balance_input = float(input("Enter Starting Balance: "))

# Create instances (objects) of Account and Customer using the input data
user_account = Account(account_number=account_input, balance=balance_input)
user_customer = Customer(name=name_input, account = user_account )

# Display the initial information entered by the user
user_customer.display_customer_info()

# Capture details for the specific action the user wants to take
transaction_type = input("Enter transaction type - deposit or withdraw : ").lower()
transaction_amount = float(input("Enter amount : "))

# Create a Transaction object which automatically executes the deposit or withdrawal
Transaction( user_account, transaction_amount, transaction_type)

# Final output to show the updated balance after the transaction
print("\n--- Final Status ---")
user_customer.display_customer_info()
