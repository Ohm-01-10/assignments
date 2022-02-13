# 6. Write a python script that repeatedly ask user to enter name and SID of students (use ‘Y’ or ‘N’). Store them in a dictionary whose keys are SID’s and values are student’s name. Perform the following operations on Dictionary :
# a. Print students details stored in the dictionary.
# b. Sort dictionary using student names.
# c. Sort dictionary using SID.
# d. Search a student details with SID and print name of that student.

d={}
c={}
choice="Y"
while choice.upper()=="Y":
    a=input("Enter your name :")
    b=input("Enter your SID :")
    d[b]=a
    c[a]=b
    choice=input("Do you wish to add more data ?")



# A
print("Print students details stored in the dictionary.")
for i in d:
    print(i,d[i])

# B
print("Sort dictionary using student names.")
lst=[]
d1={}
for j in c:
    lst.append(j)
lst.sort()
for ele in lst:
    new=c[ele]
    d1[ele]=new
for m in d1:
    print(m,d1[m])

# C
print("Sort dictionary using SID.")
lst2=[]
d2={}
for i in d:
    lst2.append(i)
lst2.sort()
for ele in lst2:
    new=d[ele]
    d2[ele]=new
for k in d2:
    print(k,d2[k])

# D
print("Search a student details with SID and print name of that student.")
user_SID=input("enter the sid to search : \n")
print("name :",d[user_SID])
