class Car:

    def __init__(self , brand , model):

        self.brand = brand
        self.model = model


    @staticmethod
    def Start():

        return "Car Started..."


    @staticmethod
    def Stop():
        
        return "Car Stopped..."



class ShubhCar_Company(Car):

    def __init__(self , carNumber , CarName , brand , model): # Yha params lene honge

        self.carNumber = carNumber
        self.carName = CarName

        super().__init__(brand , model)
        # super().Start()



shubhCar_Object_01 = ShubhCar_Company(1 , "Buggati" , "DEVILBrand" , "MODEL696") # Yha se ab args pass kerne honge



print(shubhCar_Object_01.brand)
print(shubhCar_Object_01.model)