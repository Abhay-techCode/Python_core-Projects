n=int(input("Enter a Number of ITEM\'s::"))
item=[]
for i in range (n):
    txt=input("enter a Item:")
    item.append(txt)

print("ITEM LIST ARE AS SHOWN BELOW-")

for i in range (n):
   print(f"{i+1}.{item[i]}")
