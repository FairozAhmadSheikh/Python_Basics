# # Here trying to practice OOPS Questions

# """Using input accept name and age from user make a class and pass them as arguments or attribute to object"""
# x=input("enter your  name : ");
# y=int(input("Enter Your age : "));
# class student:
#     def __init__(self,name,age):
#         self.name=name;
#         self.age=age;
# s1=student(x,y)

# print("Your name is : ",s1.name,"and  Your age is : ",s1.age)


# """ WAP To create a student class that takes name and marks of 3 subjects as arguments in a constructor 
# then create a method to print the average """

# phy=int(input("Enter Physics marks : "))
# chm=int(input("Enter Chemistry marks : "))
# math=int(input("Enter Maths marks : "))
# class Student_Result:
#     school_name="IUST "
#     def __init__(self,physics,chemistry,math):
#         self.physics=physics
#         self.chemistry=chemistry
#         self.math=math
#     def average_calc(self):
#         average=(self.chemistry+self.physics+self.math)/3
#         print("Average score  for : ",s1.name ," is :",average)

# std=Student_Result(phy,chm,math).average_calc()


# WAP to create an account class with two attributes _ balance and acc.number
# create method for debit ,credit and printing balance
x =int(input("Enter Your account number : "));
y =int(input("Enter Your Balance to start with : "));
credit=int(input("How much do you want to deposit :"));
debit=int(input("How much do you want to debit :"));
class Bank_account_details:
    def __init__(self,acc,balance):
        self.accountnumber=acc
        self.balance=balance
    def debit(self,amount):
            self.balance-=amount
            return "Account number :" + str(self.accountnumber)+ " Debited with Amount : " + str(amount) +", Balance: "+str(self.balance)
    def credit(self,amount):
            self.balance+=amount
            return "Account number :" +str(self.accountnumber)+" Credited with Amount : "+str(amount) +", Balance: "+str(self.balance)
    def bal(self):
        return "Your Total Balance "+str(self.balance)
s1=Bank_account_details(x,y)
print(s1.bal())  # balance enquiry
print(s1.credit(credit))
print(s1.debit(debit))
print(s1.bal())