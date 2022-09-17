#For tuple
n=int(input("Enter the no. of elements in tuple: "))
arr=[]
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
t=()
t=tuple(arr)
#For list
arr.clear()
n=int(input("Enter the no. of elements in list: "))
for i in range(0,n):
	d=int(input("Enter: "))
	arr.append(d)
l=[]
l=arr
add_t_to_l=[]
add_t_to_l=l+list(t)
print(add_t_to_l)
add_l_to_t=[]
add_l_to_t=list(t)+l
print(add_l_to_t)
