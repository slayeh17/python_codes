dic={}
n=int(input("Enter the number of values: "))
for i in range(n):
	key=input("Enter the key: ")
	value=input("Enter the value: ")
	dic[key]=value
print("Original Dictionary: ",dic)
dicnew=dict(sorted(dic.items()))
print("Sorted by key: ",dicnew)
sortedbyvalues={key: value for key, value in sorted(dic.items(), key=lambda item: item[1])}
print("Sorted by values: ",sortedbyvalues);
