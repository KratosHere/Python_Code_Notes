class Account:

    def __init__(self , accNum , accPass):

        self.accNum = accNum
        self.__accPass = accPass

    def reset_Password(self):

        return self.__accPass

a1 = Account(23 , "Password23")
a2 = Account(43 , "Password43")


print(a1.reset_Password())