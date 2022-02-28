#making student class
class student:

    #defining consructor

    def __init__(self,n,rn):
        self.name=n
        self.roll_number=rn

    #defining function to print the dictionary of the object containing its all details

    def printdetails(self):
        print(self.__dict__)

    # defining destructor

    def __del__(self):
        print('distruction called',self,'deleted')

#creating student object

s1=student("harsh vaish",21104071)
s2=student("om",21104039)
s3=student("lallu",21104099)
s4=student("lalballu",2110904)

#printing the details of s1

s1.printdetails()

#calling destructor

del s1

#code ends here____________________________________________________________________________________________________