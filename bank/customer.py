class customer:
        def __init__(self,id,name,ssn):
            self.name = name
            self.id = id
            self.ssn = ssn
            self.accountList = []
        def customerDetails(self):
            print ("name", self.name)
            print ("id", self.id)
            print ("ssn", self.ssn)
            print ("accountList", self.accountList)

        def changeName(self, name):
                self.name = name





