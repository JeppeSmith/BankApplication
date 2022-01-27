import sqlite3
from datetime import datetime
class transactions():
    def __init__(self):
            #,id, customerId,accountNumber,date,amount
            self.db = sqlite3.connect('Bank.db') 
            #self.customerId = customerId
            #self.accountNumber = accountNumber
            #self.id = id
            #self.date = date
            #self.amount = float(amount)
    
    def trans(self, customerId, accountNumber, amount):
        
        stmt = f"INSERT INTO Transactions (customerId, accountId, amount, date) VALUES ({customerId}, {accountNumber}, {amount}, \"{datetime.now()}\")"
        self.db.execute(stmt)
        self.db.commit()

    def withdraw_trans(self, customerId, accountNumber, amount):
        self.trans(customerId, accountNumber, float("-" + amount))

    def deposit_trans(self, customerId, accountNumber, amount):
        self.trans(customerId, accountNumber, float(amount))