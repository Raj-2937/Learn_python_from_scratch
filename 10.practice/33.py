#give a grades based on marks. 

marks = int(input("enter your marks number:"))

if (marks >= 90):
    print("grade A")
elif (marks > 70 and marks < 90):
    print("grade B")
elif (marks > 50 and  marks < 69):
    print("grade c")
else:
    print("grade d")