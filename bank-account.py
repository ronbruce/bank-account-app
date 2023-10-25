class BankAccount:
# Constructor
    def __init__(self, full_name, account_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.balance = balance
# Method of behavior for my BankAccount class or machine
# Deposit Method
    def deposit(self):
        deposit_amount = input("Enter amount you like to deposit: ")
        amount = float(deposit_amount)
        self.balance += amount
        print("Amount deposited: $" + str(amount))
        print("New balance: $" + str(self.balance))
        return self.balance
#Withdraw Method
    def withdraw(self):
        withdraw_amount = input("Withdraw amount: ")
        amount = float(withdraw_amount)
        if amount <= self.balance:
            self.balance -= amount
            print("Ammount withdrawn: $" + str(amount))
            print("New balance: $" + str(self.balance))
        else:
            overdraft_fee = 10
            print("Insufficient funds. Overdraft fee: $", str(overdraft_fee))
            self.balance -= overdraft_fee
        return self.balance
# Method for adding interest
    def interest(self):
        interest_rate = 0.00083
        interest = self.balance * interest_rate
        self.balance += interest
        print("Interest added: $" + str(interest))

# Print statement ammount and information
    def get_statement(self):
        print("Hey there, " + str(self.full_name) + "! this is your balance today.")
        print("Account number: " + str(self.account_number))
        print("Current Balance: $" + str(self.balance))

    
# Instantiate an instance of my object class BankAccount
cloud_strife = BankAccount("Cloud Strife", 21000777, 3000.00)
clive_rosfield = BankAccount("Clive Rosfield", 21000166, 100000.00)
noctis_lucis = BankAccount("Noctis Lucis Caelum",21000155, 400.00)
# calling my method

noctis_lucis.deposit()
noctis_lucis.withdraw()
noctis_lucis.interest()
noctis_lucis.get_statement()


