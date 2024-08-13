""" File I/O :  Python can be used to perform operations on data (Read and Write Data ) and this handling of data is demonstrated below 
    Types of Files:
    1 Text Files :   txt,docx,log etc
    2 Binary Files : mp4,mov,png ,jpeg
"""
#  Operations on Files
# Open a file , Read a file, close a file
"""Different Modes 
  r = open for reading
  w = open for writing but doesn't  append erases all
  x = creates a new file and open for writing
  a = open for writing , appends to the end of file
  b = binary mode
  t = text mode (Default)
  + = open a disk file for updating (read and write both)
  r+ = doesn't truncate data and stream points at starting and overwriting starts from start also we can write
  w+ = Truncates data and overwites data and also allows to read , stream is positioned at last
  a+ = read and appends stream or pointer is at last , no Truncate
"""

# Syntax 
#  f= open("Filename","mode")  mode can be read (r) or write(w)
# data=f.read()   if we pass anything in read paremeter only those no of charcters will be printed
# also we can use f.readline() to read line by line 
# f.close() 

"""Examples go from here"""
f=open("File.txt","r")
data=f.read()   # as we already printed whole file  so readline will give blank output  
print(data)   # Prints whole file

# Readline use case
line1=f.readline() # Prints first line
print(line1)
line2=f.readline() # Prints second line 
print(line2)  
f.close()   # Close file after operations as there can be a secyrity risk if left open


""""Writing To a File  """
f=open("File.txt","w")  # W for overwriting , A for Appending
f.write("This overwrites contents of File.txt ")
f.close()


# With Syntax  for file operation  , 
# With syntax automatically closes files for us so no need to mention close()

with open("new.txt",'r') as x:   
    dataa=x.read()
    print(dataa)

# Deleting a File  : We need to import an os module for the delete  functionality 
# Module is like a code library written by other programer that has some functions that can come in our use
import os 
#Mention file name or path in The fxn args
# os.remove("new.txt")  

# Practice Questions

# WAP to create a file in python and some lines of text inside it 

# Solution
# with open("Practice.txt","x") as t:
#     t.write(" I Love Java Programing ")
#     t.write(" Java is Easy to Understand ")

#WAP To replace the Word Java in above file with Python
with open("Practice.txt",'r') as q:
    d=q.read()
new_str=d.replace("Java","Python")  # Replaces java in python

with open("Practice.txt",'w') as p:  # Saves new string in our file
    p.write(new_str)

# WAP to search if particular word exists in our file
with open("Practice.txt",'r') as z:
    dq=z.read()
    searcher=dq.find("Loveed")
    if(searcher>1):
        print("Found at index",searcher)
    else:
        print("404 Not Found")

# WAP to search line number of a word that is being searched

def searcher():
    line_num=1
    data=True
    word="is"
    with open("Practice.txt",'r') as f:
        while data:
            data=f.readline()
            if(word in data):
                print("Word found at line number : ",line_num)
                return
            line_num+=1
searcher()
# Second approach for above problem
def searching():
    word = "is"
    line_n = 1
    with open("Practice.txt", 'r') as f:
        for line in f:
            if word in line:
                print("Found at line number:", line_n)
                return
            line_n += 1
    print("Word not found")

searching()

# From a file containing numbers seperated by commas, print the count of even numbers
def evenFinder():  
    count=0
    with open("Numbers.txt",'r') as f:
        data=f.read()
        # Find individual numbers first
        nums=data.split(",")
        for val in nums:
            if(int(val)%2==0):
                print(val)
                count+=1
    print("Total number of even numbers",count)
evenFinder()