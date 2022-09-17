def create():
	n=int(input("Enter the no. of elements in list: "))
	arr=[]
	for i in range(0,n):
		d=int(input("Enter: "))
		arr.append(d)
	return arr
t=()
l=[]
tl=[]
t=tuple(create())
for i in t:
	tl=[i,i**3]
	if(tuple(tl) not in l):
		l.append(tuple(tl))
print(l)	
