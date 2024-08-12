# # Functions 
# """ Block of statements that perform a specific Task, Functions are used to reduce redundant code and make code resuable4
#    Syntax of function  ==   def function_name(params) : return something and at last call fxn ==> function_name(argument) 
# """
#  # Function defination with parameters
# def sum(a,b):
#     return a+b;
# # Function calls and Arguments
# print(sum(10,20))

# # Function that greets user when called 
# x=input("Enter Your Name : ") or "FERoz"
# def greet(name):
#     return "Hello : "+name;

# print(greet(x))

# # Average of three Numbers  using fxn
# a=int(input("Enter number one : ")) 
# b=int(input("Enter number two : "))
# c=int(input("Enter number three : ")) 

# def average(d,e,f):
#     return "average is ", (d+e+f)/3
# print(average(a,b,c))

# # Types of Functions 
# """ Built in Functions and User Defined Functions
#  (a)   Built in Functions :  functions that are by default present and have some functionality like examples below 
#        print(),len(),type(),range()
#        built in functions are already written in python and their logic also is written
#  (b)   User Defined Functions : functions defined by user for their own work, their logic etc is to be written by user
#     e.g user create function for sum,mul,div,subtract etc 
# """
# # WAF to print the length of list (list in parameter)
# list=[1,2,4,"This",True]
# def length_find(a):   # Fxn Defination
#     return len(a)
# print("The length of list is : ",length_find(list))  # Fxn call


# # WAF to print a  list in single line using fxn 
# def print_list(a):
#     for i in range(len(a)):
#         print(list[i],end=" ")

# print(print_list(list))

# # Convert USD to INR
# n=int(input("How many USD want you to convert to INR : "))
# def converter(b):
#     return b*83.63  # Considering 1 USD equal to 83.63 INR
# print("You will receive : ",converter(n)," INR")

# # WAF To find the factorial of n using functions (n is a parameter)
# def fact():
#     n2=int(input("Enter Num to find Factorial"))
#     fact=1
#     for i in range(n2,n2>=1,-1):
#         fact=fact*i
#     return fact
# print(fact())

# """ Recursion means when a function calls itself repeatedly  it is said to be recursive funnction , 
# Loops and recursion are inter-related the work that can be done by loops can also be done by recursion and vice-versa
# """
# # Example for Recursion
# def view(n):
#     if(n==0):  # Condition to avoid infineite Loop also known as a Base Case
#         return
#     print(n)
#     view(n-1)  # Recursion as it calls itself 
# view(5)        # Function Call

# # Factorial using recursion
# def fct(a):
#     if a==0 or a==1:
#         return 1;
#     else:
#         return a * fct(a-1)
# print(fct(5))

# # WAP to calculate sum of first n natural numbers using recursion
# def sum(n):
#     if n==0 :
#         return 0
#     else:
#         return n+sum(n-1)
# print(sum(5))

# # WAP To print all elements in a list using recursion hint : we can use  index and list as parameters

list=['a','b','c','d']
def itter(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    itter(list,index+1)  # This goes recursion
print(itter(list))