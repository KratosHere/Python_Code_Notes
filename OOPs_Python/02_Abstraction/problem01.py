# Create Account class with 2 attributes - balance and account number create methods debit(-) , credit(+) & getBalance.


class Account:

    def __init__(self , accNum , accBalance):

        self.Account_Number = accNum
        self.Account_Balance = accBalance


    def debit(self , withdrawal):

        return f"{withdrawal}Rs Debited, Final Balance: {(self.Account_Balance) - withdrawal} for Account_Number: {self.Account_Number}"

    def credit(self , amtAdded):

        return f"{amtAdded}Rs Credited, Final Balance: {(self.Account_Balance) + amtAdded} for Account_Number: {self.Account_Number}"


    def getBalance(self):

        return f"Current Bank Balance: {self.Account_Balance}"


myAccount1 = Account(501 , 45680)
myAccount2 = Account(432 , 66340)

# print(myAccount1.debit(10000))
# print(myAccount2.credit(2000))


# print(myAccount1.getBalance())
print(myAccount2.getBalance())