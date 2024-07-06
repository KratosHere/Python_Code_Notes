class Student:

    def __init__(self , name , age , gender):

        self.name = name
        self.age = age
        self.gender = gender # Say i wanna delete this prop/attr/data



s1 = Student("Vansh Jain" , 34 , "Female")
s2 = Student("Abhishek" , 23 , "not Applicable")

del s1.gender # gender property has been deleted!

del s2 # Whole Object s2 has been deleted!