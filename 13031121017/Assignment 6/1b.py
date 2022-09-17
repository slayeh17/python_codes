dic={}
n=int(input("Enter the number of values: "))
for i in range(n):
	key=input("Enter the key: ")
	value=input("Enter the value: ")
	dic[key]=value
print("Original Dictionary: ",dic)
sorted_values=sorted(dic.values())
dic_sorted={}
keys=dic.keys()
for j in sorted_values:
	for i in keys:
		if(dic[i]==j):
			dic_sorted[i]=j
print("Sorted: ",dic_sorted)
