# Dictionaries refering to objects as in js
# Stores data in key value pairs
# Dictionaries dont have indexes and are accesed used keys
# Dictionaries are mutable like arrays 
# Dictionaries dont allow to use duplicate keys

dict={
    "name":"Feroz",
    "age":22,
    "phone":7889521098,
    "subjects":("AI","ML"),
    "isGraduate":True,
    "keyword":["Grad","PG","UG"]
}

print(dict)
print(dict["phone"])
# changeing any parameter in dictionart
dict["age"]=23
dict["name"]="Feroz Ahmad Sheikh"
print(dict)
print(dict["subjects"])
dict["subjects"]=("ML","AI")
print(dict)
# Appending works in same way as updating any value for key 
# For example i want to add "University" :"IIT Patna " in dictionary it can be added as
dict["University"]="IIT Patna"
print(dict)
print(type(dict))

# Nested Dictionaries  = Dictionary into Dictionary
student_data={
    "name":"Fairoz",
    "age":23,
    "extra":{
        "surname":"Sheikh",
        "address":"Gulshan_Bagh",
        "phone":123456,
        "additional":{"likes_Tea":"Yes",
                      "likes_Coding":"Yes"
                      }
    }
}
print(student_data)

# Accessing particular value of nested Dictionary
print(student_data["extra"]["address"])
print(student_data["extra"]["phone"])
print(student_data["extra"]["additional"]["likes_Coding"])

# Medthods for Dictionaries
# Printing Keys 
print(student_data.keys())  # Gives keys  but not for nested 
print(student_data["extra"].keys())  # Find keys in nested dicts

#printing Values
print(student_data.values())

# Printing Items # return keys and values in form of Tuples
print(student_data.items())

# Get method used for printing value for a key 
""" Differnce between accessing data using direct key and using get method is that if key is not present get shows none but
but traditional method shows error Below is an example
"""
d={"name":"Ali",
   "age":22}
# print(d["age2"])    # This  traditional method will shows error  as key is wrong but below methods wont
print(d.get("age2"))  # This  get method shows  none instead of error

# Update values in dictionary 
# Traditional method
d["ph"]=788952
print(d)
# using update method
d.update({"school":"GVE"})
print(d)



                                            # Sets 
"""Sets are mutable  but elements of sets are immutable ,sets are  unique collection of unordered elements  
Sets and dictionaries both dont have any order which means it does not have indexes and order of output can
be unexpected sometimes , We can add and remove elements in sets this tells sets are mutable  .
Note :
       1. ✅ Boolean , int, Float, string and Tuple can be stored in Sets.
       2. ❌ Dictionaries and Lists cant be saved  in Sets as these are immutable.
"""
   
det={1,2,3,4,5,2 ,"abc","abc"}  # As we have a dupliacte item 2 it will be considered only once.
print(type(det))
print(det)  # Ignores Duplicate Values

# How to create an empty Set 

st={}    # This is Dictionary not set 
stt=set()  # This Creates an Empty Set
print(type(st))   # This is Dictinory
print(type(stt))  # This is Set

# Methods in Sets

# Pop => removes random value 
det.pop()
print(det)

# Add => adds element to set

det.add("Hello")
print(det)

# Remove => remove specific element

det.remove("abc")
print(det)


# Clear => Empties  the set

dteeee={1,2,3,4,5,8}
dteeee.clear()
print(dteeee)

# Union and Intesection in same way as in Maths 
set1={1,2,3,4,5,6,7,8,9}
set2={"a","b","c","d","e","f",1}
set3={1,2,3,5}

# Union combines and gives output
print(set1.union(set2))

# Intersection gives common 
print(set1.intersection(set3))