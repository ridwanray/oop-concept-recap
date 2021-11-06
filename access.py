class Person:
    def __init__(self, name, age, genger):
        self.__name = name
        self.__genger= genger
        self.__age = age
p1 = Person('ade',23, "male")
print(p1.__name)
