class Student:
    def __init__(self, name , age):
        self.__name = name
        self.__age = age

    def get_name(self, ):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self, ):
        return self.__age

    def set_name(self, age):
        self.__name = age

studenti1 = Student("Amant", "13")

print("Name:", studenti1.get_name())

studenti1.set_name("DerbiTV")
print("updated name:", studenti1.get_name())

print("Age:", studenti1.get_age())

studenti1.set_age("15")
print("updated age:", studenti1.get_age())

