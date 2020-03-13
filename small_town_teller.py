



class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


    def unique_id:
        bank_ids = []
        for i in self.id:
            if i not in bank_ids:
                bank_ids.append(i)
print (bank_ids)




class my_class(object):
    def __init__(self):
        self.lis1 = []
        self.dict1 = {}

    def __nonzero__(self):
        return bool(self.lis1 or self.dict1)


"""
obj = my_class()
if obj:
    print "Available"
else:
    print "Not available"



    def unique_owner:
        self.owner = self.first_name + self.last_name
        bank_owners = []
        for i in self.owner:
            if i not in bank_owners:
                bank_owners.append(i)
"""



class Account:
    def __init__(self, number, type, owner, balance):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = balance

    def unique_number:
        bank_numbers = []
        for i in self.number:
            if i not in bank_numbers:
                bank_numbers.append(i)

    number =
    type =
    owner =
    balance =

class Bank:
    bank.add_customer # Adding a customer to the bank
    bank.add_account # Adding an account to the bank
    Removing an account from the bank
    bank.deposit # Depositing money into an account
    bank.withdrawal # Withdrawing money from an account
    bank.balance_inquiry # Balance inquiry for a particular account


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
