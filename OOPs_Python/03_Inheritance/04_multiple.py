class Mother:

    @staticmethod
    def MotherProp1():

        return "Beauty From Mother"

class Father:

    @staticmethod
    def FatherProp1():

        return "Brain From Father"



# Ye CHILD -> FATHER AND MOTHER DONO KE PROPERTIES KO INHERIT KAREGI!


class Child(Father , Mother):

    @staticmethod
    def ChildProperty():

        return "CHILD PROPERTY"


child_Object_01 = Child()

print(child_Object_01.MotherProp1())
print(child_Object_01.FatherProp1())
print(child_Object_01.ChildProperty())