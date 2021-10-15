class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10


print(Math.add10(4))
c = Math.add10(5)
print(c)
#A static method does not need instance creation
#before it can called. It can be callled on the class directly
