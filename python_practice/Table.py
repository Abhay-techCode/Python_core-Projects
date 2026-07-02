#It's a Table Generator

num=int(input("Enter a Number:"))

print(f"The Table of {num}")
#here range with ( inc , excl)
for i in range (1,11): 
    print(f"{num} * {i} = {num*i}")     
