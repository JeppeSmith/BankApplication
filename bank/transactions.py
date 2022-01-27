import sqlite3
from datetime import datetime
class transactions():
    def __init__(self):
            self.db = sqlite3.connect('Bank.db') 
    
    def trans(self, customerId, accountNumber, amount):
        
        stmt = f"INSERT INTO Transactions (customerId, accountId, amount, date) VALUES ({customerId}, {accountNumber}, {amount}, \"{datetime.now()}\")"
        self.db.execute(stmt)
        self.db.commit()

    def withdraw_trans(self, customerId, accountNumber, amount):
        self.trans(customerId, accountNumber, float("-" + amount))

    def deposit_trans(self, customerId, accountNumber, amount):
        self.trans(customerId, accountNumber, float(amount))