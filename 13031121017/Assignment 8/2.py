f=open("file.txt","rt")
c=len(f.readlines())
print("Number of lines: ",c)
f.close()