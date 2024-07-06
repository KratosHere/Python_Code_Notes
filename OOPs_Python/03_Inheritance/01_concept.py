class Car:

    @staticmethod
    def Start():

        return "CAR STARTED..."

    @staticmethod
    def Stop():

        return "CAR STOPPED..."



class TataNano(Car): # Car ki properties and Methods ko inherit ker rhe!

    def __init__(self , name):

        self.name = name
    



car1 = TataNano("Fortuner")
car2 = TataNano("Buggaattii")

# print(car1.name)

print(car1.Start())
