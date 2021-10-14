class Person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1
        Person.add_person()
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1 



# print(Person.number_of_class())
p1 = Person('time')
# print(Person.number_of_people)
p2 = Person('jill')
print(Person.number_of_people_())

# Person.number_of_people = 8
# print(p1.number_of_people)

