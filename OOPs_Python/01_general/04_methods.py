class Student:

    

    def __init__(self,name,age):

        self.name = name
        self.age = age


    def sayHello(self):

        return f"Hello {self.name}"


    # Static Method

    @staticmethod
    def Hello_Static():

        return "Hello STATIC"


    # Now create multiple methods!

s1 = Student("Arjun",22)


print(s1.Hello_Static())