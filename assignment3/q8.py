#Given Sets :
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

# A
# Create a new set of all elements that are in Set1 and Set2 but not both.
print("A :")
a=set1-set2
print(a)

# B
# Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.
print("B :")
b=set1^set2^set3
print(b)

#C
# Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3.
print("C")
intersection_12=set1.intersection(set2)
intersection_13=set1 & set3
intersection_23=set2 & set3
all_intersection=set1 & set2 & set3
a=intersection_12|intersection_13|intersection_23 - all_intersection
print(a)

# D
# Create a new set of all integers in the range 1 to 10 that are not in Set1.
print("D :")
set4={1,2,3,4,5,6,7,8,9,10}
m=set4-set1
print(m)

#E
# Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3.
union=set1|set2|set3
print("E :")
e=set4-union
print(e)