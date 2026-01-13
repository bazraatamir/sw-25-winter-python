# class Person:
#     def greate(self):
#         print("test")

# class Student(Person):
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#         self.grades=[]

  


#     def add_grade(self,grade):
#        self.grades.append(grade)
#        return True
#     def avg_grade(self):
#         n=len(self.grades)
#         s=sum(self.grades)
#         return s/n
#     def get_age(self):
#         return self.__age

# student_1=Student("bat",18)
# student_1.add_grade(80)
# student_1.add_grade(95)
# student_1.add_grade(70)
# print(student_1.avg_grade())


# print(student_1.get_age())
# student_2=Student("od",18)
# student_2.add_grade(60)
# student_2.add_grade(65)
# student_2.add_grade(60)
# print(student_2.avg_grade())

# student_3=Student("ganaa",18)
# student_3.add_grade(70)
# student_3.add_grade(95)
# student_3.add_grade(100)
# print(student_3.avg_grade())
from abc import ABC,abstractmethod

class Person(ABC):
    
    @abstractmethod
    def introduce(self):
        pass

class Student(Person):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
        self.grades=[]

    def add_grade(self,grade):
       self.grades.append(grade)
       return True
    
    def avg_grade(self):
        n=len(self.grades)
        s=sum(self.grades)
        return s/n
    
    def get_age(self):
        return self.__age
    
    def introduce(self):
        print(f"сайн байна уу? миний нэр {self.name},миний нас {self.__age}, би оюутан")


class Teacher(Person):
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def introduce(self):
        print(f"сайн байна уу? миний нэр {self.name},миний нас {self.__age}, би Багш")
        

test = [Student("bat",18),Teacher("tsestgee",26)]        

