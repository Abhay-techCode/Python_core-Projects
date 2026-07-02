"""
i=0
student={}

num=int(input("Enter Number of Student : "))
f = open("student.txt","a")
while i<num:
    name = input("Enter student Name : ")
    age = int(input("Enter Your Age : "))
    mark = int(input("Enter Total Marks : "))
    student["name"] =name
    student["age"] = age
    student["mark"]= mark

    f.write(str(student))
    i+=1


f.close()
"""

q = open("student.txt","r")
text = q.read()

search = input("Enter The Name : ")
i=0
for student in text:
    if student["name"] == search:
        print(text)
        q.close()
