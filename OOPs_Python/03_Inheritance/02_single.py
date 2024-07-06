
class Parent1:

    @staticmethod
    def doSomething():

        return "Doing Something"


class Child1(Parent1):

    def __init__(self):

        pass



object1 = Child1()

print(object1.doSomething())