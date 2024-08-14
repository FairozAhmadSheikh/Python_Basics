# OOPS  => object oriented programing
# To map with the real world scenerios we started using objects in the code , This is known as Object Oriented Programming.
#  Class is the blueprint for anything  and Object is an instance of the class
# example we create blueprint of car and define what should it have this is class and actual product waht is made is object.

class student:    # Creates Class 
    name="Feroz";
    age=22
s1=student()     # Creates Object
print(s1.name,s1.age)
s2=student()
s2.name="Sheikh"
s2.age=66
print(s2.name,s2.age)

# Constructor : all classes have a  __init__() function that is always executed  when the object is being initiated or created
# init accepts many parameter but self is the first one that it accepts and we can pass many arguments like belwo
class Students:
    def __init__(self,fullname,age):   # Init() always takes parameter self , self points to object s3 below (or in Javascript This)
        self.name=fullname   #Attribute name
        self.age=age         #Attribute Age
        print("Adding student to database as you have created objected so __init__() gets automatically called")
s3=Students("Fairoz ahmad sheikh",22)
print(s3.name,s3.age)

# Self parameter is the refrence to the current instance of the class, and is used to access the variables belonging to the class
# Data or variables that are used to store data in class are known as attributes
# Parameterized constructors are the constructor that conatin more than self parameter 
# Default constructors are the constructors that have only self parameter