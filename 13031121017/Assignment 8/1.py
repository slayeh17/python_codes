n=int(input("Enter the number of lines to be read: "))
f=open("file.txt","rt")
for i in range(n):
    print(f.readline())
f.close()