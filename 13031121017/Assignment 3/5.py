a=[]
s=input("Ente a string: ")
a=s.split(" ")
w=input("Enter the prefix: ")
i=0
for x in a:
	a[i]=w+x
	print(a[i],end=" ")
	i+=1
print()
