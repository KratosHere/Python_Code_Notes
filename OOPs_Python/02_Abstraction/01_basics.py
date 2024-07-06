class Car:

    def __init__(self):

        self.acc = False
        self.brk = False
        self.cth = False

    def start(self):

        self.cth = True
        self.acc = True
        return "CAR STARTED!!!"

    def stop(self):

        
        self.cth = True
        self.brk = True
        return "CAR STOPPED!!!"
        


LAMBO = Car()

print(LAMBO.start())
print(LAMBO.stop())