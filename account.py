class BankAccount:
    account_counter = 1000
    def _init_(self, name, balance=0):
        self.name = name
        self.__balance = balance
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        



    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount} , now balance is {self.__balance}")
        else:
            print("deposit amount is must bre greater than 0")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"withdraw {amount}. new balance is {self.__balance}")
        else:
            print(" withdraw amount must bre greater than 0 and less than or equal to the balance")

    def display_account_info(self):
        print(f"Account Number: {self.account_number},name : {self.name}. balance: {self.__balance}")

class SavingsAccount(BankAccount):
    
    def init(self, name, balance=0, interest_rate=0.02):
        super().init(name, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest of {interest}. New balance is {self.get_balance()}.")

class CurrentAccount(BankAccount):
    def _init_(self, name, balance=0, overdraft_limit=5000):
        super()._init_(name, balance)
        self.overdraft_limit = overdraft_limit