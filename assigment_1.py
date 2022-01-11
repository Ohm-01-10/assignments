
# QUESTION 1

print("please enter the numbers in the format _,_,_")
num1,num2,num3=(input("enter three numbers")).split(",")
avg=int(num1)+int(num2)+int(num3)/3
print(avg)


# QUESTION 2

# # 2. Write a python program to compute a person's income tax. Assume following
# # tax laws:
# # • All taxpayers are charged a flat tax rate of 20%.
# # • All taxpayers are allowed a $10,000 standard deduction.
# # • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
# # • Gross income must be entered to the nearest penny.
# # Gross Income and the number of dependents must be asked from the user.
# # Hint:
# # Taxable income = Gross Income - Standard deduction - (Dependent deduction
# # * No. of dependents)
# # Tax = Taxable Income * Tax Rate
#

total_income=int(input("Enter your Total Income"))
no_of_dependents=int(input("enter the no of dependents"))
standard_deduction=10000
taxable_income=total_income-standard_deduction-(no_of_dependents*3000)
tax=taxable_income*0.20
print(f"your total income is ${total_income} \nstandard deduction is ${standard_deduction} \ndeduction on dependents is ${no_of_dependents*3000} \ntax is {tax}")


# QUESTION 3

student=["SID", "Name", "Gender", "Course_Name", "CGPA"]
entry="Y"
lst1=[]
while entry=="Y":
    lst = []
    for i in range(len(student)):
        print("enter your",student[i])
        value=input(" ")
        lst.append(value)
    lst1.append(lst)
    entry=input("another entry ? Y for yes and N for no")
print(lst1)


# QUESTION 4


no_of_entries=0
req=["name","marks"]
lst1=[]
while no_of_entries!=5:
    lst=[]
    for i in req:
        print("enter your",i)
        values=input(" ")
        lst.append(values)
    lst1.append(lst)
    no_of_entries+=1
for entries in lst1:
    print(entries)

# Question 5


color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color)
color1=color.copy()
color1.remove(color[3])
print(color1)
# # Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
color[3:5]=["Purple"]
print(color)



