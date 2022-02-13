# Write a python program to print Fibonacci sequence also print average of the resultant Fibonacci series.
a=0
b=1
n=10
lst=[a,b]
for i in range(n-2):
	c=a+b
	lst.append(c)
	a=b
	b=c
print(f"fibonacci series of first {n} elements :")
print(*lst,sep=',')
print(f"Average of first {n} fibonacci number is {(sum((lst))/len(lst))}")