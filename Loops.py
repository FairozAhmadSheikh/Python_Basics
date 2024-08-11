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