class Student:

    # Default Constructor
    # def __init__(self):

    #     pass

    # Parameterized constructors

    def __init__(self , fullName , age):

        self.NAME = fullName
        self.AGE = age
        # print("DATA ADDED!")


s1 = Student("Sahil" , 23)
s2 = Student("Akshat" , 34)


print(f"{s1.NAME} is {s1.AGE} years old , {s2.NAME} is {s2.AGE} years old")