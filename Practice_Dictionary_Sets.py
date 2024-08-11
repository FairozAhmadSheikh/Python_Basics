# WAP To store any two words with meanings in dictionary
dictionary={
    "apple":"Fruit Red in Color",
    "port":["Used for Listening to servers","Used to connect Hardware "]
}
print(dictionary)



# WAP to check number of rooms required for teaching each subject in  a list individually in single room from list below
subjects=["English","Math","AI","ML","CSE","Electrical","Electronics","English","AI","CSE"]
# Create a set first from above data and obtain its length and done 
rooms=set(subjects)
print("Number of rooms required : ",len(rooms))


# WAP to enter marks of three subjects from user and save them in a dictionary also calculate percentage 
marksheet={}
subject1=int(input("Enter marks for subject ones : ")) 
marksheet.update({"Subject1":subject1})
subject2=int(input("Enter marks for subject two : ")) 
marksheet.update({"Subject2":subject2})
subject3=int(input("Enter marks for subject three : ")) 
marksheet.update({"Subject3":subject3})
print(marksheet)
print("Total Percentage  : " ,((subject1+subject2+subject3)/300)*100,"%.")
