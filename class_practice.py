class Bank_account():

    def __init__(self,accountno,balance):
        self.balance=balance
        self.accountno=accountno

    def credit(self,amount):
        self.balance=self.balance+amount


acc=Bank_account("12345",100)

acc.credit(500)

print(acc.balance)
        