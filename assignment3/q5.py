# Write a python program to print following pattern.
# ABCDEFGHIJK
#  ABCDEFGHI
#   ABCDEFG
#    ABCDE
#     ABC
#      A


st="ABCDEFGHIJK"
for i in range(len(st)//2+1):
	for column in range(0,i):
		print(" ",end="")
	print(""+st[0:len(st)-2*i:])        #Omitting multiple of 2 at every column.
