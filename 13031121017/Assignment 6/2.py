student={"name":"","assignment":[],"test":[],"lab":[]}
avg_assi=0
avg_test=0
avg_lab=0
student["name"]=input("Enter the name: ")
for i in range(1,5):
	d=int(input(f"Enter the assignment marks {i} :"))
	student["assignment"].append(d)
	avg_assi+=d/4
for i in range(1,3):
	d=int(input(f"Enter the test marks {i} :"))
	student["test"].append(d)
	avg_test+=d/2
for i in range(1,3):
	d=float(input(f"Enter the lab marks {i} :"))
	student["lab"].append(d)
	avg_lab+=d/2
final_score=0.1*avg_assi+0.7*avg_test+0.2*avg_lab
print("Final Score: ",final_score)
if(final_score>=90):
	print("Grade: A")
elif(final_score>=80 and final_score<90):
	print("Grade: B")
elif(final_score>=70 and final_score<80):
	print("Grade: C")
elif(final_score>=60 and final_score<70):
	print("Grade: D")