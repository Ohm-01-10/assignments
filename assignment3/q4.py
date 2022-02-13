keys=(4,5,6,7,8,9,10)
values=("D","C","C+","B","B+","A","A+")
name=('Poor','Below Average','Average','Good','Very Good','Excellent','Outstanding')
dct={}
dct1={}
for i in range(len(keys)):
	dct[keys[i]]=values[i]
print(dct)
for i in range(len(keys)):
	dct1[keys[i]]=name[i]
print(dct1)

cgp=int(input("enter  ur cgp :"))
print(f"Your grade is {dct[cgp]} and {dct1[cgp]} performance.")

