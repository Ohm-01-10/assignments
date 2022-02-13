# Given the sets below, write python statement to:
# Set1= {1, 2, 3, 4, 5}
# Set2= {2, 4, 6, 8}
# Set3= {1, 5, 9, 13, 17}
# a. Create a new set of all elements that are in Set1 and Set2 but not both.
# b. Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
# c. Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.
# d. Create a new set of all integers in the range 1 to 10 that are not in Set1.
# e. Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.

set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}
# A
print("A :")
a=set1-set2
print(a)

# B
print("B :")
b=set1^set2^set3
print(b)

#C
print("C :")
lst=[]
lst1=[]
union=set1 | set2 | set3
for i in union:
    lst.append(i)
for ele in lst:
    if lst.count(ele)==2:
        lst1.append(i)
print(set(lst1))

# D
print("D :")
set4={1,2,3,4,5,6,7,8,9,10}
m=set4-set1
print(m)

#E
print("E :")
e=set4-union
print(e)