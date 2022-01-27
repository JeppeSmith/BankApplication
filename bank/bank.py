#Skriv funktionen så att förändring görs i det objekt det gäller
#Skicka sedan en "uppdatering" till datasource som skickar en query och uppdaterar databasen
from os import access
from datasource import datasource
from customer import customer
from Account import Account
from transactions import transactions

class bank():
    def __init__(self):
        self.ds = datasource()
        self.ts = transactions()
        self.ds.getAll()
        self.Account = []
        self.customers = []
        self.transactions = []
        self.loadData()
        self.runSystem()
        
        

    def addCustomer(self):
        pass
                   
    def loadData(self):
        f = open('Customer.txt', 'r')
        for line in f:
            id, name, ssn = line.strip().split(':')
            self.customers.append(customer(id, name, ssn))

        f = open('Account.txt', 'r')
        for line in f:
            balance, accountNumber, customerId, accountType = line.strip().split(':')
            self.Account.append(Account(balance, accountNumber,customerId, accountType))

    def runSystem(self):
        print('Välkommen!')
        while True:
            print(' 1:Withdraw\n 2:Deposit\n 3:Show Account\n 4:Print all customers\n 5:Add Customer\n 6:Change customer name\n 7:Create account\n 8:Show account transactions\n 9:Show customer information\n 10:Remove account\n 11:Remove customer\n x for exit ')
            
            i = input()
            if i == '1':
                self.withdraw()
            elif i == '2':
                self.deposit()
            elif i == '3':
                self.showAccount()
            elif i == '4':
                self.getCustomers()
            elif i == '5':
                self.addCustomer()
            elif i == '6':
                self.updateCustomer()
            elif i == '7':
                self.createAccount()
            elif i == '8':
                self.showTransactions()
            elif i == '9':
                self.customerDetails()
            elif i == '10':
                self.close_account()
            elif i == '11':
                self.removeCustomer()
            elif i == 'x':
                exit()

    def withdraw(self):
        c_id = input("Enter customer id\n")
        accounts = []
        for a in self.Account:
            if c_id == a.customerId:
                accounts.append(a)
        for a  in accounts:
            print(f"account number: {a.accountNumber}  balance:{a.balance}")            
        a_id = input("Enter account number\n")
        for a in accounts:
            if a.accountNumber == a_id:
                amount = input("enter amount to withdraw\n")
                a.withdraw(amount)
                self.ts.withdraw_trans(c_id, a_id, amount)
                return
        print("Invalid account number")
        return
        #Valt customer
        #Valt konto
        #Valt antal kr du tog ut
        #konto.withdraw
        #self.ds.updateAccount(konto)
        #self.ds.updateAccount()

    def deposit(self):
        c_id = input("Enter customer id\n")
        accounts = []
        for a in self.Account:
            if c_id == a.customerId:
                accounts.append(a)
        for a  in accounts:
            print(f"id: {a.accountNumber}  balance:{a.balance}")            
        a_id = input("Enter account number\n")
        amount = input("enter amount to deposit\n")
        for a in accounts:
            if a.accountNumber == a_id:
                a.deposit(amount)
                self.ts.deposit_trans(c_id, a_id, amount)
                return
        print("Invalid account id")
        return

    def showAccount(self):
        c_id = input("Enter customer id\n")
        accounts = []
        for a in self.Account:
            if c_id == a.customerId:
                accounts.append(a)
        for a in accounts:
            print(f"id: {a.accountNumber}")            
        a_id = input("Enter account number\n")
        for a in accounts:
            if a.accountNumber == a_id:
                a.showAccount()
                return
        print("Invalid account number")

    def getCustomers(self):
        c = self.customers
        for c in self.customers: 
            print(c.id, c.ssn, c.name)

    def updateCustomer(self):
        c_id = input("Enter customerid to change\n")
        for c in self.customers:
            if c_id == c.id:
                d = input("enter new name\n")
                c.changeName(d)
                self.ds.update_by_id(c_id, d)
                return
        print("Couldn't find customer with id")
        return 


    def createAccount(self):
        c_id = input("Enter CustomerId to open account for\n")
        a_id  = int(self.Account[-1].accountNumber) + 1
        accountType = input("enter AccountType")
        a = Account(0, a_id, c_id, accountType)
        self.ds.createAccount(a)
        return

        
    def showTransactions(self):
        pass
    def customerDetails(self):
        pass
    def close_account(self):
        b = input("SELECT SSN TO REMOVE ACCOUNT FROM\n")
        a = input("SELECT ACCOUNT NUMBER TO REMOVE\n")
        self.ds.close_account(a)
        pass
    def removeCustomer(self):
        a = input("SELECT ID TO REMOVE\n")
        self.ds.remove_by_id(a)
    def exit():
        quit()
