n=int(input("Enter the no. of elements: "))
arr=[]
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
t1=()
t1=tuple(arr)
lt=[]
print(t1)
while True:
	print("Enter the elements you want to insert or enter '.' to exit: ")
	d=input()
	if(d=='.'):
		break
	if int(d) in t1:
		lt.append(int(d))
	else:
		print("Element not in tuple")
t2=()
t2=tuple(lt)
print(t2)
