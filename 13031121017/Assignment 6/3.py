def create_dict():
    dic={}
    n=int(input("Enter the number of values: "))
    for i in range(n):
        key=input("Enter the key: ")
        value=input("Enter the value: ")
        dic[key]=value
    return dic

dic1={}
print("Enter for dictionary 1: ")
dic1=create_dict()
dic2={}
print("Enter for dictionary 2: ")
dic2=create_dict()

for i in dic1.keys():
    if(i in dic2.keys()):
        print(f"Found {i}")
dic1.update(dic2)
print(dic1)