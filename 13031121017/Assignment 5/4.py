def create():
	n=int(input())
	arr=[]
	for i in range(0,n):
		d=int(input("Enter: "))
		arr.append(d)
	return arr
t1=()
t2=()
print("Enter the no. of elements in tuple 1: ")
t1=tuple(create())
print("Enter the no. of elements in tuple 2: ")
t2=tuple(create())
l=[]
t3=()
for i in range(0,len(t1)):
	l.append(t1[i]%t2[i])
t3=tuple(l)
print(t3)
