f=open("file.txt","at")
l=[]
n=int(input("Enter the number of items in the list: "))
for i in range(n):
    d=input("Enter: ")
    l.append(d)
for i in l:
    f.write(i)
    f.write("\n")
f.close()