'''dict = {
    "Name" : "Yajat",
    "Roll no" : 59,
    "Marks" : [98,96,94],
}

print(dict) 
print(len(dict))
print(type(dict))

print(dict["Name"])

dict["Name"] = "Naam"
dict["Location"] = "Delhi  "
print(dict)

null_dict={}


null_dict["Tu nala hai"] = ["Kaustubh"]
print(null_dict)'''

#Nested Dict

'''student = {
    "Name" : "Yajat",
    "Subjects" : {
        "phy" : 98,
        "chem" : 76,
        "Math": 85
    }
}

print(student["Subjects"]["phy "])

#Dictionary methods
dict = {
    "Name" : "Yajat",
    "Roll no" : 59,
    "Marks" : [98,96,94],
    "Location" : "Mumbai"
}

#all keys
print(dict.keys())

#all values
print(dict.values())

#all items
print(dict.items())

#return key according to the value
print(dict.get("Name"))

#Toal no of keys
print(len(dict))

#Update
dict.update({"Country" : "India", "age" : 20})
print(dict)
'''


#Store the foloowing with meaning

'''table = "a piece of furniture", "list of facts & figures"
cat = "a small animal"'''

'''dictionary = {
    "cat" : "a small animal",
    "Table" : ["a piece of furniture", "a list of facts and figures"]
}
print(dictionary)'''

'''set = {"python","java","python","javascript","java","python","java","c++","C"}
print(len(set))'''

'''#WAP to enter marks of 3 subjects from the user and store them in dictionary. Start with an empty dict and add one by one. Use subject name as key and marks as value
dict = {}

a = int(input("Enter first subject marks:-"))
dict.update({"Phy" : a})
b = int(input("Enter second subject marks:-"))
dict.update({"Chem" : a})
c = int(input("Enter third subject marks:-"))
dict.update({"Maths" : a})

print(dict)
'''

# store 9 and 9.0 as diff in set

'''values = {9,"9.0"}
print(values)
print(type(values))'''

values = {
    ("float" ,9.0),
    ("int,9")
}

print(values)