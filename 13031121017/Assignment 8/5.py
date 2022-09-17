finame=input("Enter the file name: ")
pattern=input("Enter the string pattern: ")
f=open(finame,"rt")
c=0
content=f.read()
content_list=content.split(" ")
for word in content_list:
    if pattern == word:
        c+=1
print(content_list)
print("Number of occurence: ",c)
f.close()