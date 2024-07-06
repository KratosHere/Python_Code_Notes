
class Parent1:

    @staticmethod
    def doSomething1():

        return "Doing Something - Prop of Parent 1"


class Child1(Parent1):

    @staticmethod
    def doSomething2():

        return "Doing Something - Prop of Child1."



class child2(Child1):

    @staticmethod
    def doSomething3():

        return "Doing Something - Prop of Child2"


object1 = Child1()
object2 = child2()

print(object1.doSomething1())

print(object2.doSomething2())
print(object2.doSomething1())