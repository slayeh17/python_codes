def fact(n):
	f=1
	for i in range(1,n+1):
		f*=i
	return f
def Comb(n,r):
	return fact(n)/(fact(n-r)*fact(r))
def pascal_triangle(n):
	for i in range(0,n):
		for s in range(i,n):
			print(" ",end="")
		for j in range(0,i+1):
			print(int(Comb(i,j)),end=" ")
		print()
n=int(input("Enter number of rows: "))
pascal_triangle(n)
