# # Conditionals, operators, strings etc Basic Things
# print("Welcome to Game ");
# consent=input("Do you want to Play? ").lower();
# if consent=="yes" :
#     print("Lets Begin with ❤️❤️❤️");
# else:
#     quit();
# score=0
# question=input("What does CPU Stand for ? ").lower();
# if question=="central processing unit":
#     score+=1;
#     print("Correct");
# else:print("Incorrect")
# question=input("What does GPU Stand for ? ").lower();
# if question=="graphics processing unit":
#     score+=1
#     print("Correct");
# else:print("Incorrect")
# question=input("What does LU Stand for ? ").lower();
# if question=="logical unit":
#     score+=1
#     print("Correct");
# else:print("Incorrect")
# question=input("What does JNU Stand for ? ").lower();
# if question=="jawaharlal nehru university":
#     score+=1
#     print("Correct");
# else:print("Incorrect")

# print("Your Score is " +str(score))
# if ((score/4)*100)> 75.0 :
#     print("Passed")
# else:print("Failed")


# print("Voting going to start")
# age=int(input("What is Your age"))
# if age>80:
#     print("You are Very senior stay home safe")
# elif age>=18:
#     print("Eligible")
# else: print("Yet Yonger")

# print("Greatest between Three Numbers")
# number1=int(input("Enter 1st Number"))
# number2=int(input("Enter 2nd Number"))
# number3=int(input("Enter 3rd Number"))
# print("Entered Numbers are :" ,number1,number2,number3)
# if number1>=number2 and number1>=number3:
#     print("Number 1 is greatest",number1)
# elif number2>=number3:
#     print("Number 2nd is greatest",number2)
# else:
#     print("Number 3rd is greates",number3)
str="hello World!"
print(str.endswith("!"))  #True
# Operations on strings
#UpperCase, Lowercase, Capitalize
print(str.upper())  #Uppercase
print(str.lower())  #Lowercase
print(str.capitalize()) #Capitalize
#Finding Element
print(str.find("llo"))  #Gives index of place
# Replacing Element in strings
print(str.replace("hello","Hi"))