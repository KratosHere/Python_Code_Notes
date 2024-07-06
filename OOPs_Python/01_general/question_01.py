# Create student class that takes name and marks of 3 subjects as arguements in constructor, then create a method to print the average


# Can pass a list also which contains marks


# class Student:

#     def __init__(self  , name , Pmarks , Cmarks , Mmarks):

#         self.name = name
#         self.Pmarks = Pmarks
#         self.Cmarks = Cmarks
#         self.Mmarks = Mmarks


#     def getAverage(self):

#         return (self.Pmarks + self.Cmarks + self.Mmarks) / 3



# s1 = Student("Arjun"  , Pmarks=76 , Mmarks=79 , Cmarks=80)

# PCM_Aggregate = s1.getAverage()


# print(f"{s1.name} got {PCM_Aggregate} percentage for PCM aggregate")

class Student:

    def __init__(self , name ,  MARKS):

        self.name = name
        self.MARKS = MARKS


    def getAverage(self):

        avg = 0
        for mark in (self.MARKS):

            avg += mark

        # avg = avg/3
        avg = avg//3
        
        return avg


s1 = Student("Keshav" , [6,2,1])

print(s1.getAverage())