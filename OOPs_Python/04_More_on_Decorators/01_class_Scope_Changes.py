# class Person:

#     name = "CHANGE THIS NAME"

#     def changeName(self , name):

#         self.name = name


# p1 = Person()

# p1.changeName("NIKHIL")

# print(p1.name)
# print(Person.name)


class Person:

    name = "CHANGE THIS NAME"

    def ChangeName(self , name):

        # Person.name = name

        # Or

        self.__class__.name = name




p1 = Person()
p1.ChangeName("SHUBHASHISH")

print(p1.name)
print(Person.name)