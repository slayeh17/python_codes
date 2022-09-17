n=int(input("Enter the no. of elements: "))
arr=[]
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
print("Original List: ",arr)
t=arr[0]
arr[0]=arr[len(arr)-1]
arr[len(arr)-1]=t
print("Edited List: ",arr)
