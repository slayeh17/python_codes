n=0
c=0
sum=0
while True:
	n=int(input("Enter a number: "))
	if(n==0):
		break
	sum+=n
	c+=1
print("Sum: ",sum)
print("Average: ",sum/c)
