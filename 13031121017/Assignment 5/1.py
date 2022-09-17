def ins():
	n=int(input("Enter the no. of elements: "))
	arr=[]
	for i in range(0,n):
		d=int(input("Enter: "))
		arr.append(d)
	return arr

l1=[]
l2=[]
l1=ins()
l2=ins()
t1=()
t2=()
t1=tuple(l1)
t2=tuple(l2)
print(t1,t2)
temp=()
#swapping
temp=t1
t1=t2
t2=temp
print(t1,t2)
