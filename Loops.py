# Loops are used for repetation of code or anything that needs to be run for several times
# Loops are used to repeat instructions
# print something many times

# While and For Loop
count =0             #Initialization
while count<=5:      # Condition
    print("Hello",count)   # what to do (Operation)
    count= count+1   # Iterator


#  WAP  To Print Multiplication Table of N 
num=int(input("Enter The Number for  which You want to print  Multiplication Table : "))
i=1
while i<=10 :
    print(num," X ",i,": ",num*i)
    i+=1

# WAP To Search a number in a Tuple
num2=int(input("Enter a Number To Search "))
tup=(1,2,3,4,5,6,7,1,2,3,7)
found=False
i=0
while i<len(tup):
    if tup[i]==num2:
        found=True
        print("Found at index ", i)
        
    i+=1;
if found==False:
    print("Not found")

# Break and Continue
# Break is used to terminate the loop completely
# Continue is used to skip the current iteration and continue the rest of loop 
# Continue Terminates execution in current itteration  and continues execution of loop with next iteration

# Example for Break if count reaches 10 loop Terminates
i=0;
while i<=100:
    if i==10: # This loop Terminates and stops printing when index reaches 10
        break;
    else:
        print(i)
    i+=1

# Continue  Use case  : Skipping Current iteration
# WAP to obtain all even numbers using continue and while

i=0;
while i<=10:
    if(i%2 !=0):   
        i=i+1
        continue
    else:
        print(i)
        i+=1



# For LOOP
"""For Loop is used at places  where there is need of sequential traversal like strings , Lists , Tuples
  we can also add an else statement at last of our for loop which tells us the loop ended , else in for loop is
  optional"""

lister=["abc","def",1,2,3,4,5]
for element in lister: # Prints Everything in List 
    print(element)

# WAP To find any element in list using for loop

lister=["abc","def",1,2,3,4,5]
to_search="def"
founded=False
for element in lister: # Prints Everything in List 
    if(to_search==element):
        founded=True
        print("Element Found",element)
else:
    print("Loop ends here")


# We can also run loop using specific range using range function 
# range() function returns a sequence of numbers starting from zero  to the mentioned range with itration of +1
# range() accepts three things start? ,stop, step?   where ? = denotes optional 
# Range doesnt consider last or stop index ==> loops runs length-1 times

# Simple syntax of range  only stop 
for i in range(15):
    print(i)   
# Other syntax of range  start , stop , step
for i in range(1,10,2):
    print(i)
# Last syntax
for i in range(2,4):  # start and stop only mentioned
    print(i)
# Use case of range 
listed_coin=["dhani","bari","bitcoin","cobra"]
for i in range(1,len(listed_coin),1):
    print(listed_coin[i])

# WAP To print 100 to 1 using range 
for i in range(100,0,-1):
    print(i);


# Pass statement is a null statement that does nothing , it used as a place holder for future code
for i in range(5):
    pass
print("Loops executes here only if pass is present , if pass is removed it wont work")


# Practice Questions 

# write a program for finding sum of first n natural numbers (using while)
numbers=int(input(" Enter sum of how many numbers do you want : "))
i=0;
sum=0;
while i<=numbers:
    sum=sum+i
    i=i+1;

print("Sum of Numbers is ",sum)

# WAP To find the factorial of first n Numbers
# e.g Factorial of 5 is 5*4*3*2*1
numbers1=int(input("Enter the number which we want to find factorial of : "))
fact=1
for i in range(numbers1,0,-1):
    fact = fact*i;
print("Factorial of  ",numbers1," : ",fact)