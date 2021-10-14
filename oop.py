class Dog:

    classAttriName = 'Ridwan'
    classAttributeValue = 'initial'
 
    def __init__(self, name, age, Passed=None):
        self.name = name
        self.classAttributeValue = Passed
        
    def get_name(self):
        return self.name, self.classAttriName


    def get_age(self):
        return self.age,self.classAttriName

    def set_age(self,age):  #modifying the self.age
        self.age = age
    # def add_one(self, x):
    #     # print(self.mynam e, 'coming from one')
    #     return (x+1)
  
    # def bark(self):
    #     print('bark')

  
d = Dog('Tim', 34,'passed')
print(d.classAttributeValue)
# d.set_age(30)
# print(d.get_age())
 



# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade #0-100

#     def get_grade(self): 
#         return self.grade


# class Course: 

#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
  
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
        
#         return value / len(self.students)

# s1 = Student('Tim', 19, 95)
# s2 = Student('Bill', 19, 75)
# s3 = Student('Jnill', 19, 65)
 
# course = Course('Science', 2)  
# course.add_student(s1) 
# course.add_student(s2)
# print(course.add_student(s3))
# # print(course.students)
# print(course.students[0].name, course.students[0].age)  
# print(course.get_average_grade())