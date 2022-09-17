def count(sen):
	u=0
	l=0
	for i in sen:
		if(i>='A' and i<='Z'):
			u+=1
		elif(i>='a' and i<='z'):
			l+=1
	print("No. of Upper case characters: ",u)
	print("No. of Lower case characters: ",l)
	
s=input("Enter a sentece: ")
count(s)
