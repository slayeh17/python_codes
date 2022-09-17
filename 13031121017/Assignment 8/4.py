f1=open("file.txt","rt")
f2=open("file2.txt","at")
for line in f1:
    f2.write(line)
f1.close()
f2.close()