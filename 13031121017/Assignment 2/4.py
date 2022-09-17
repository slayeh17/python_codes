a=int(input("Enter lower bound: "))
b=int(input("Enter upper bound: "))
c=0
for i in range(a,b+1):
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				c=1
				break
		if(c==0):
			print(i)
		else:
			c=0
