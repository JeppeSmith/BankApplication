import sqlite3
from Account import Account
from customer import customer

class datasource:
    def __init__(self):
        self.db = sqlite3.connect('Bank.db') 
        print(self.db)
        self.cur = self.db.cursor()

    def update_by_id(self, id, name):
        try:
            stmt = f"UPDATE Customer SET Name = \'{name}\' WHERE Id = {id}"
            s = self.db.execute(stmt)
            self.db.commit()
            stmt2 = f"SELECT * FROM CUSTOMER WHERE Id = {id}"
            return self.find_by_id(id)
        except:
            print("tepm")
            return -1

    def find_by_id(self, id):
        try:
            stmt = f"SELECT * FROM CUSTOMER WHERE Id = {id}"
            for row in self.cur.execute(stmt):
               return(f"{row[0]}:{row[1]}:{row[2]}\n")
        except:
            return -1

    def createAccount(self, account: Account):
        stmt = f"INSERT INTO Account (balance, accountNumber, customerId, accountType) VALUES ({account.balance}, {account.accountNumber}, {account.customerId}, \"{account.accountType}\")"
        self.db.execute(stmt)
        self.db.commit()

    def createCustomer(self, customer: customer):
        stmt = f"INSERT INTO Customer (Id, Name, SSN) VALUES ({customer.id}, \"{customer.name}\", {customer.ssn})"
        self.db.execute(stmt)
        self.db.commit()

    def updateBalance(self, Account):
        pass

    def removeAccount(self, Account):
        stmt = f"DELETE FROM Account WHERE accountNumber = {Account.accountNumber}"
        self.db.execute(stmt)
        self.db.commit()
    def remove_by_id(self, id):
        try:
            r = self.find_by_id(id)
            stmt = f"DELETE FROM Customer WHERE Id = {id}"
            self.db.execute(stmt)
            self.db.commit()
            return r
        except:
            return -1


    def close_account(self, accountNumber):
        try:
            r = self.find_by_id(id)
            stmt = f"DELETE FROM Account WHERE accountNumber = {accountNumber}"
            self.db.execute(stmt)
            self.db.commit()
            return r
        except:
            return -1
    
    def getAll(self):
        stmt = f"SELECT * FROM Customer"
        f = open('Customer.txt', 'w')
        for row in self.cur.execute(stmt):
            f.write(f"{row[0]}:{row[1]}:{row[2]}\n")

        stmt = f"SELECT * FROM Account"
        f = open('Account.txt', 'w')
        for row in self.cur.execute(stmt):
            f.write(f"{row[0]}:{row[1]}:{row[2]}:{row[3]}\n")

        stmt = f"SELECT * FROM Transactions"
        f = open('Transactions.txt', 'w')
        for row in self.cur.execute(stmt):
            f.write(f"{row[0]}:{row[1]}:{row[2]}\n")
        #Hämtar ALL data om ALLA customers och ALLA konton och ALLA transaktions och skriver det till sin text fil

