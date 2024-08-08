# Type Conversion 
a="10";
print(type(a))
b=10;
print(int(b),type(b))

#Lists are Mutable but strings are not 
data =[1,2,3,4,6,8,9,0]
string="Python"
# Type checking
print(type(data))
print(type(string))

#Slicing can be done on both the strings as well as Lists
#Negative indexing is allowed in both strings as well as Lists
print(string[1:3])
print(data[2:4])
print(string[-5:-2])