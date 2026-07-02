dict={
    "name":"abhay",
    "roll":18,
    "age":21,
    "gender":True

}


print(dict)

print(dict.items())

print(dict.keys())

print(dict.get("age"))

print(dict.values())

dict.update({"name":"varad"})

print(dict.values())

a=dict.pop("name")
print(a)
print(dict)
dict.update({"name":"varad"})
print(dict)

a=dict.popitem()

print(a)

dict.clear()
print(dict)

dict={"name":"varad","roll":21,"age":22,"addresss":"ganaga nagar"}

a = "name" in dict
print(a)

print(dict["name"])