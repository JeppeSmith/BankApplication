class Account():
        def __init__(self,balance, accountNumber,customerId,accountType):
            self.balance = float(balance)
            self.customerId = customerId
            self.accountType = accountType
            self.accountNumber = accountNumber

        def deposit(self, depositAmount):
            self.balance += float(depositAmount)
            print(f"new balance: {self.balance}")
            return


        def withdraw(self, withdrawAmount):
                if self.balance >= float(withdrawAmount):
                        self.balance -= float(withdrawAmount)
                        print(f"new balance: {self.balance}")
                        return
                print(f"Couldn't withdraw that amount, balance is {self.balance}")


        def showAccount(self):
                print(f"Balance {self.balance} Account Number: {self.accountNumber} customerId {self.customerId} AccountType {self.accountType}")

        def createAccount(self):
                pass

                






