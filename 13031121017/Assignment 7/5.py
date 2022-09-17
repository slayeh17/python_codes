def make_sum(s,n):
	return s+n
	
s=0
N=int(input("Enter the number of numbers: "))
for i in range(0,N):
	n=input("Enter a number: ")
	s=make_sum(s,int(n))
print("Sum: ",s)
