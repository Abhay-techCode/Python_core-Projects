# List is a collection of elements or set of elements
# It consist of different datatype elements
# List are Mutanble _ means we can modify there existing data

fruit = ["Mango","apple","banana"]

print(fruit)

fruit[1] = "Pineapple"  # We can access elements by Index 0 to n-1

print(fruit)

# append() method used to add element in list at last
marks = []
print(marks)

marks.append(34)
print(marks)
marks.append(94)
marks.append(24)
marks.append(84)
marks.append(34)
print(marks)

for item in marks:
    print("Marks = ",item)

marks.sort()            #As name suggested its a sorting in ascending order
print("The sorted marks: ",marks)

marks.sort(reverse=True)    # For descending order Sorting
print("The reversed : ",marks)

class_marks = marks.copy() # This would return a shallow copy of List itself

print(class_marks)

print(len(marks)) # return length (Total Number of elements )

print(marks.count(34)) # Returns appearance of any element

marks.insert(2,67) #Add element at particular index

print(marks)

marks.extend([24,25,26])
print(marks)

i = marks.index(34) # return index of element
print(i)

marks.remove(94) # Remove element
print(marks)
'''(method) def pop(
 index: SupportsIndex = -1,
 /
) -> Any

Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.
'''
marks.pop()
print(marks)

marks.clear() # Clear List Completely
class_marks.clear() # Remove all elements in List
print(marks)
