class  Pet:
    classAttribute = "amAClassAttribute"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
        # return (f"I am {self.name} and I am {self.age} years old")
    def speak(self):
        # raise NotImplementedError('Subclass must override this')
        print('I dont know how to say ')

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color=color

    def speak(self): 
        print(self.name,  'Meow')
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} and I am {self.color}")
     

class Dog(Pet):

    def speak(self):
        print(self.name, 'Bark')


class Fish(Pet):
    pass


 
p = Pet('Petty', 19)
p.show()

c  = Cat('Catty', 34,'yellow')
c.speak()
c.show()

d = Dog('Doggy', 89)

d.speak()

f = Fish('fishhy', 20)
f.speak()

 




# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print('Meow')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         print('Bark')

