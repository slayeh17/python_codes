n=int(input("Enter the no. of elements: "))
arr=[]
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
arr.sort(reverse=True)
print("Second Largest Number: ",arr[1])
