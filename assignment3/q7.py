# Write a python program to print Fibonacci sequence also print average of the resultant Fibonacci series.

a=0            #First two number of fibonacci series is 0 and 1
b=1
n=10           #n is the nth position of fibonacci number needed(end pos)

lst=[a,b]      #list to store all n fibonacci numbers.Starting with 0 and 1.

for i in range(n-2):        #loop till n-2 as first two element 0 and 1 are already entered.
	c=a+b                   #temp element to support execution.
	lst.append(c)
	a=b
	b=c
print(f"fibonacci series of first {n} elements :")
print(*lst,sep=',')         #Printing every element of lst and seperating by comma, simultaniously.
print(f"Average of first {n} fibonacci number is {(sum((lst))/len(lst))}")      #taking Average.