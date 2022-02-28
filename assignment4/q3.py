#taking input from user
n1=int(input('please enter your first number:\n'))
n2=int(input('please enter your second number:\n'))

#calculating quotient
def quotient(n1,n2):
    print('the quotient of the numbers is:',n1/n2)

#calculating remainder
def remainder(n1,n2):
    print('the remainder of the numbers is:',n1%n2)

quotient(n1,n2)
remainder(n1,n2)
print()
#_______________(a) checking the callability of the functions__________________________

print('quotient is callable:',callable(quotient))

print('remainder is callable:',callable(remainder))
print()
#---------------(b) checking values to be non zero--------------------------------------

if (n1 and n2)!=0:
    print('both the numbers are non zero')

else:
    print('some of the numbers is zero')
print()
#------------------(c) adding (4,5,6) to the result and filtering out values greater than 4_________________

lst=[4,5,6]
lst.append(n1//n2)
lst.append(n1%n2)

x=list(filter(lambda x:x>4,lst))
print('the no. greater than 4:',x)

#-------------------(d) converting the above result into set____________________________________________________
print()
set_x=set(x)
print('the set of the numbers greater than 4:',set_x)
#-------------------------------(e) making the set immutable------------------------------------------

frozenset(set_x)

#---------------------------------(f)calculating the hash value of the maximum no. in the above set---------
print()
print('hash value of the maximum no.:',hash(max(set_x)))

#code ends here