#Tuple related
#Tuple--it is datatype in python used to store elements of datatype
"""                 --ordered
                    --immutable
only operations or methods provide are count,index not possible to add element or remove or replace


#Tuple accessing
tup=("ram","sham","nayan",12)

print(len(tup)) #length of tuple

print(tup[0:5])

tup1=("abhay","patil")

tup3=tup+tup1
print(tup3)


a=()  //empty tuple
a=(1,) //single element tuple
a=(12,24,5,89) //multi element tuple


"""

tup=("ram","abhay","ram","varad")
print(tup.count('ram'))

print(tup.index('ram'))