#Array are used to store Elements of same datatype only
#list are the datatype - used to store elements of diff datatype
#List having index and operations / functions are associated with them
#THE FUNCTIONAL RESULT NOT ONLY PRINATABLE ITS ACTUAL WORKED AND CHANGES WILL OCCURE
'''operations of List
    1.sort()
    2.reverse()
    3.append()-------add at last
    4.insert(3,8)-----add 8 at index 3
    5.pop(2)------remove element at index 2
    6.remove(21)------remove element from list
    '''
"""
fruit=['apple','banana','mango','pineapple','strawberry']

print(len(fruit))

li=[12,23,89,20,21]
print(li)
print(li[0:])
print(li[:5])
li.sort()
li.append("Abhay")
print(li)
""" 


#SORTING AN LIST IN DESCENDING ORDER

num=[12,90,56,45,96,22]
num.sort(reverse=True)
print(num)


"""
student=["abhay","varad","nayan","manish","ajay"]
student.append("sham")
print(student)
student.sort()
print(student)

i=len(student)
print(i)
student.reverse()
print(student)

student.reverse()
print(student)

student.insert(1,"Akshay")
print(student)
"""