class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person('time')

p2 = Person('jill')


# Person.number_of_people = 8
# print(p1.number_of_people)

