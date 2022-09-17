n=int(input("Enter the no. of elements: "))
arr=[]
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
print("Original List: ",arr)
arr.reverse()
print("Reversed List: ",arr)
