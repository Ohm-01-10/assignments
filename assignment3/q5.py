# Write a python program to print following pattern.
# ABCDEFGHIJK
#  ABCDEFGHI
#   ABCDEFG
#    ABCDE
#     ABC
#      A


st="ABCDEFG"
for i in range(len(st)//2+1):
	for column in range(0,i):
		print(" ",end="")
	print(""+st[0:len(st)-2*i:])
