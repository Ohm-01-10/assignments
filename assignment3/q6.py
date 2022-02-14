# 6. Write a python script that repeatedly ask user to enter name and SID of students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and values are student’s name. Perform the following operations on Dictionary :
# a. Print students details stored in the dictionary.
# b. Sort dictionary using student names.
# c. Sort dictionary using SID.
# d. Search a student details with SID and print name of that student.

SID_Name={}
Name_SID={}
choice="Y"
while choice.upper()=="Y":
    name=input("Enter your name :")
    SID=input("Enter your SID :")
    SID_Name[SID]=name
    Name_SID[name]=SID
    choice=input("Do you wish to add more data ?")



# A
print("Print students details stored in the dictionary.")
for i in SID_Name:
    print(i,SID_Name[i])

# B
print("Sort dictionary using student names.")
lst=[]        #Creating list to sort
d1={}         #Creating a sorted dictionary
for j in Name_SID:
    lst.append(j)
lst.sort()     #Name inserted and Sorted.
for ele in lst:
    corresdonding_SID=Name_SID[ele]
    d1[ele]=corresdonding_SID              #adding key value pairs in d1.
for m in d1:                               #m for element indexing.
    print(m,d1[m])

# C
print("Sort dictionary using SID.")
lst2=[]
d2={}
for i in SID_Name:
    lst2.append(int(i))
lst2.sort()
for ele in lst2:
    corresdonding_Name=SID_Name[str(ele)]
    d2[ele]=corresdonding_Name
for k in d2:
    print(k,d2[k])

# D
print("Search a student details with SID and print name of that student.")
user_SID=input("enter the sid to search : \n")
if user_SID in SID_Name:
    print("name :",SID_Name[user_SID])
else:
    print(f"{SID_Name[user_SID]} not found in entries.")