class Student:

    def __init__(self , phy , chem , math):
    
        self.phy = phy
        self.chem = chem
        self.math = math
    
    
    @property
    def percentage(self):

        return str((self.phy + self.chem + self.math) // 3) + "%"



student01 = Student(56,60,49)

print(f"Percentage ATTR before Updation : {student01.percentage}")

student01.phy = 78

print(f"Percentage ATTR AFTER Updation : {student01.percentage}")