keys_cgpa=(4, 5, 6, 7, 8, 9, 10)
Grades=("D", "C", "C+", "B", "B+", "A", "A+")
Performance=('Poor', 'Below Average', 'Average', 'Good', 'Very Good', 'Excellent', 'Outstanding')
Cgp_grade={}
Cgp_performance={}
for i in range(len(keys_cgpa)):
	Cgp_grade[keys_cgpa[i]]=Grades[i]
print(Cgp_grade)
for i in range(len(keys_cgpa)):
	Cgp_performance[keys_cgpa[i]]=Performance[i]
print(Cgp_performance)

cgp=int(input("enter  ur cgp :"))
print(f"Your grade is {Cgp_grade[cgp]} and {Cgp_performance[cgp]} performance.")

