# Object Bnane se pehele Uss object ki class bntii => Blueprint


class Student:

    name = "Rahul"
    age = 21
    DOB = "14 July 2006"


# Creating Objects (Instances) by using the blueprint

student_01 = Student() # This student1 Is an Object now
student_02 = Student() # This student2 Is an Object now
student_03 = Student() # This student3 Is an Object now



print(student_01) # This will Say yeah this is an object!
print(student_01.name) # Same name will be of all the students!
print(student_01.age) # Same age will be of all the students!

print(student_02.age) # Same age will be of all the students!