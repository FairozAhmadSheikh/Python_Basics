# WAP ask user to type his three favorite movies and store them in a list
list=[]
movie1=input("Enter Your first favoritemovie : ")
list.append(movie1)
movie2=input("Enter Your first favoritemovie : ")
list.append(movie2)
movie3 =input("Enter Your first favoritemovie : ")
list.append(movie3)
print("Your Favorite movies are : ", list)

# WAP To check if a list contains pallendrome or not
data=[1,2,3]
data2=data.copy()
data2.reverse()
if data==data2:
    print("palendrome")
else:
    print("Not pallendrome")

# WAP to count the number of students with Grade "A" in the tupple below
tupple=("A","A","B","C","B","B","A","C","C","D")
print(tupple.count("A"))
# now push the tupple into a blank list and sort them from A TO D
listt=["A","A","B","C","B","B","A","C","C","D"]
listt.sort()
print(listt)




