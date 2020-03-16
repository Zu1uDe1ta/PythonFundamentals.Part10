
class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def _str_(self):
        return f"{self.id} identifies as {self.first_name}_{self.last_name}"

    def _repr_ (self):
        return f"{self.id} identifies as {self.first_name}_{self.last_name}"

class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"{self.number}, {self.type}, {self.owner},"

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = {}
    # Adding a customer to the bank, pull from class Person parameters
    def add_customer(self, person):
        self.customers.append(person.id)
    # Adding an account to the bank, pull from class Account
    def add_account(self, account):
        if account not in self.accounts:
            self.accounts[account.number] = account.balance
        else:
            print("Account Already Exist")
    # Depositing money into an account, you need account number and balance
    def deposit(self, account_number, amount):
        self.accounts[account_number] += amount
        print("Deposited:", amount)
    # Withdrawing money from an account
    def withdrawal(self, account_number, amount):
        self.accounts[account_number] -= amount
        if amount > self.accounts[account_number]:
            print("Insufficient Balance")
        else:
            self.accounts[account_number] -= amount
            print("Amount Withdrawn:", amount)
    # Balance inquiry for a particular account
    def balance_inquiry(self, account_number):
        print(f"Balance= {self.accounts[account_number]}")


self.add_account
# Removing an account from the bank, pull from class Account
self.deposit
self.withdrawal
self.balance_inquiry

















"""
Constraints

When attempting to register a customer, the customer id must be unique.
When attempting to add an account, the user associated with said account must already registered as a customer.
When attempting to add an account, the account number must be unique.

from small_town_teller import Person, Account, Bank

zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.balance_inquiry(1001)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.balance_inquiry(1001)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.balance_inquiry(1001)
"""




"""
    def unique_id(self):
        bank_ids = []
        for i in self.id:
            if i not in bank_ids:
                bank_ids.append(i)
        print (bank_ids)

    def unique_owner:
        self.owner = self.first_name + self.last_name
        bank_owners = []
        for i in self.owner:
            if i not in bank_owners:
                bank_owners.append(i)

      def unique_number(self):
        bank_numbers = []
        for i in self.number:
            if i not in bank_numbers:
                bank_numbers.append(i)              

"""
