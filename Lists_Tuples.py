# Type Conversion 
a="10";
print(type(a))
b=10;
print(int(b),type(b))

#Lists are Mutable but strings are not which means any index value can be changed 
data =[1,2,3,4,6,8,9,0]
string="Python"

# Type checking
print(type(data))
print(type(string))

#Slicing can be done on both the strings as well as Lists
#Negative indexing is allowed in both strings as well as Lists
#If we forget any stating or ending index it will by default be 0 and len(str)

print(string[1:3])
print(data[2:4])
print(string[-5:-2])

# List Methods 
dataset=[9,8,7,6,5,4,9,3,2,1,0,9]
# Counting Number of times elemnet is present
print("Number of occourences is :",dataset.count(9))
# Finding the position of element First index 
print(dataset.index(1))
# Adding element to List
dataset.append(10)
print(dataset)
# Sorting a List  accending order
dataset.sort()
print(dataset)
# Sorting a List  decending order
dataset.sort(reverse=True)
print(dataset) 
# Reverse a list
dataset.reverse()
print(dataset)
#add element at any index
dataset.insert(0,2)
print(dataset)
# Remove first occourence of an element 
dataset.remove(0)
print(dataset)
# Deleting something at an index
dataset.pop(0)
print(dataset)

# Tupple is immutable sequences of values which means you cant change a particular value
tup =(10,20,30,60,10,10)
print(tup)
# Metbods of Tuples   #
# Find Index of element
print(tup.index(30)) 
# Find Number of occurences
print(tup.count(10))