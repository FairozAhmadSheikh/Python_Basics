# Here trying to practice OOPS Questions

"""Using input accept name and age from user make a class and pass them as arguments or attribute to object"""
x=input("enter your  name : ");
y=int(input("Enter Your age : "));
class student:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
s1=student(x,y)

print("Your name is : ",s1.name,"and  Your age is : ",s1.age)


""" WAP To create a student class that takes name and marks of 3 subjects as arguments in a constructor 
then create a method to print the average """

phy=int(input("Enter Physics marks : "))
chm=int(input("Enter Chemistry marks : "))
math=int(input("Enter Maths marks : "))
class Student_Result:
    school_name="IUST "
    def __init__(self,physics,chemistry,math):
        self.physics=physics
        self.chemistry=chemistry
        self.math=math
    def average_calc(self):
        average=(self.chemistry+self.physics+self.math)/3
        print("Average score  for : ",s1.name ," is :",average)

std=Student_Result(phy,chm,math).average_calc()