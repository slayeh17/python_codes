n=int(input("Enter the no. of elements: "))
arr=[]
pos=0
neg=0
zero=0
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
	if(d>0):
		pos+=1
	elif(d==0):
		zero+=1
	else:
		neg+=1
print("Positive Numbers: ",pos)	
print("Negative Numbers: ",neg)
print("Zeroes: ",zero)
