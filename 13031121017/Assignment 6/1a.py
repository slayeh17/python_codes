dic={}
n=int(input("Enter the number of values: "))
for i in range(n):
	key=input("Enter the key: ")
	value=input("Enter the value: ")
	dic[key]=value
print("Original Dictionary: ",dic)
dicnew=dict(sorted(dic.items()))
print("Sorted: ",dicnew)
