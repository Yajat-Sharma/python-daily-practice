collection = {1,2,3,4,4,4,4,4,7}

print(collection)
print(type(collection))
print(len(collection))

#Empty set
z = set()

#Addition of elements
collection.add(10)
print(collection)

#Removal of elements
collection.remove(7)
print(collection)

#Removes a random value
print(collection.pop())
print(collection.pop())

#Empties the set
collection.clear()
print(collection)

#union of setss
a = {1,3,5,7,9,11}
b = {5,6,7,8,9}

print(a.union(b))

#Intersection of sets
print(a.intersection(b))
