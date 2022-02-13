# Write a python script to print next date of input date. It must meet following conditions(use if-elif)
# C1:1<=month<=12
# C2:1<=day<=31
# C3:1800<=year<=2025
# Write a python script to print next date of input date. It must meet following conditions(use if-elif)
# C1:1<=month<=12
# C2:1<=day<=31
# C3:1800<=year<=2025
# # E.g.:
# Input: Day - 28
# Month -02
# Year -1999


day=input("Day :")
month=input("Month :")
year=input("Year :")
user_date=f"{day}/{month}/{year}"
a=user_date.split("/")
days_months={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
name={1:"january",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
x=int(a[1])
if int(year)>=1800 and int (year)<=2025 and int(month)>=1 and int(month)<=12 :
                  #storing int of month in x for calling value from dictionary days_months
    if int(a[1])<12 and int(a[0])==days_months[x]:
        a[0]=1
        a[1]=int(a[1])+1
        print("Next Date :", a[0], "/", a[1], "/", a[2])
    elif int(a[0])<days_months[x]:
        a[0]=int(a[0])+1
        print("Next Date :", a[0], "/", a[1], "/", a[2])
    elif int(a[1])==12 and int(a[0])==days_months[x] :
        a[0]=1
        a[1]=1
        a[2]=int(a[2])+1
        print("Next Date :", a[0], "/", a[1], "/", a[2])
    if int(day)>days_months[x]:
        print(f"Day out of range of {name[x]}")

elif int(month) > 12:
    print("Month is out of Range.")
