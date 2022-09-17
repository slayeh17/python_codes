n=int(input("Enter the no. of elements: "))
arr=[]
e=0
o=0
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
	if(d%2==0):
		e+=1
	else:
		o+=1
print("Even Numbers: ",e)	
print("Odd Numbers: ",o)
