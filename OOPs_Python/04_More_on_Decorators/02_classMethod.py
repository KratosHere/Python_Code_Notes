# Whi same kaam, ker rhe jo 01 Me kiya

class Person:

    name = "CHANGE THIS NAME"

    @classmethod
    def ChangeName(cls , name): # cls -> CLASS

        cls.name = name # YE CHANGE DIRECTLY CLASS KE ATTRIBUTES ME HONE WAALA HAI!!



p1 = Person()
p1.ChangeName("Dadddy KRATOS")

print(p1.name)
print(Person.name)