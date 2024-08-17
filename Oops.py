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
    # If some data in class reamains same place it outside constructors
    college_name="IUST Awantipora"  # Class attribute
    def __init__(self,fullname,age):   # Init() always takes parameter self , self points to object s3 below (or in Javascript This)
        self.name=fullname   # object Attribute name
        self.age=age         # object Attribute Age
        print("Adding student to database as you have created objected so __init__() gets automatically called")
s3=Students("Fairoz ahmad sheikh",22)  # Instance attribute
print(s3.name,s3.age,s3.college_name)

# Self parameter is the refrence to the current instance of the class, and is used to access the variables belonging to the class
# Data or variables that are used to store data in class are known as attributes
# Parameterized constructors are the constructor that conatin more than self parameter 
# Default constructors are the constructors that have only self parameter



"""Class and Instance attributes
Attribute meany any data or variable like in above we have attribute name and age
 Two Types of Attributes:
 1: Class attributes : These attributes remain same
 2: Instance or object attributes : These are values passed to class values and can be different """



"""Methods are the Functions that belong to objects
 Functions that are written inside the classes are known as Methods"""
# Example 
n=input("Enter Car Name")
m=input("Enter Car Model")
class Car:
    company="Mahindra and Mahindra Corp"
    def __init__(self,carName,carModel):
        self.carName=carName
        self.carModel=carModel
    def start(self):
        print("Car Starts ",self.carName," Grrrrrrrrrrrrrrrr")
c1= Car(n,m).start()    # Fxn Call and create object at same Time


"""Static methods :
 static methods are the methods without self parameter (Which means they work at class level)"""

# Decorator is something that changes the behaviour of the normal function 
"""Decorator allows us to wrap another function in order to extend the behaviour of the wrapped function
 without permenantly modifying it """
class Hello:
    @staticmethod # Decorator
    def hello():
        print("hello")
h1=Hello.hello()



# Important Topics  for OOPs are
#  Abstarction  : means hiding the implementation details of a class and showing the essential feature  to the user.
# Encapsulation : means wrapping data and functions into single unit(object)
# Inheritance   : 
# PolyMorphisim : 