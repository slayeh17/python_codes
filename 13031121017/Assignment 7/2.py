def create():
	n=int(input("Enter the no. of elements: "))
	arr=[]
	for i in range(0,n):
		d=int(input("Enter: "))
		arr.append(d)
	return arr
def mul(l=[]):
	m=1
	for i in l:
		m*=i
	return m
l=[]
l=create()
print("Product: ",mul(l))
