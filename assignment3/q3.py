# Write a Python program to create a list of tuples with the first element as the number and Second element as the square of the number.
# E.g. list = [3, 9, 10]
# Output: [(3, 9), (9, 81), (10, 100)]


lst=[1,2,3,4]
sq=lambda x: x**2
lst1=[]
for i in lst:
	new=sq(i)
	k=(i,new)
	lst1.append(k)
print(lst1)