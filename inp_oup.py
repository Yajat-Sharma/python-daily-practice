'''f = open("demo.txt","r")
data = f.readline()
line2 = f.readline()

print(data)

f.close()'''

# writeing a fileee
'''
f = open("demo.txt","w")
f.write("I want to learn javascript")
f.close()
'''
# appending new data into fileeee

'''f=open("demo.txt","a")
f.write("\nThen i'll move to python libraieis")
f.close()
'''
# creating a new file

'''f = open("New.txt","a")
f.write("This is a new flile and a example of file")
f.close()
'''
# new file creation

'''f = open("newfile.txt","a")
f.close
'''
 
# r =  if i open the file in r  then  or reading
# r+ = if the file is opened in  r+   then it is for reading and writing pointer in the starting
'''w = if it is opened in w if earses the file data to zero length or 
if the file is not there it creates a new file for reading and writing'''
# W= = opne for reading and writing . new file is created if it does not exist, otherwise truncted
# a = open for r and w . New file is created if not there . s
# tream postioned at the end of the fileeee 
# a+ = open for reading and writing . new file is created if new does not exist . the stream is postioned at the end of the fileeee
'''
f = open("demo.txt","a+")
f.write("abc")
f.close()'''

'''with open("demo.txt","r") as f:
    data = f.read()
    print(data)

with open("demo.txt","w") as f:
    f.write("This is new data addded afterwards")'''

# To delete a file we can write this
'''import os
os.remove("demo.txt")'''

#Practice Questions

'''with open("practice.txt","r") as f:
    data = f.read()

new_data = data.replace("Java","Python")
print(new_data)

with open("pracctice.txt","w") as f:
    f.write(new_data)
'''
'''def checkforword():
    word = "learning"
    with open("practice.txt","r") as f:
        data  = f.read()
        if(data.find(word) !=-1):
            print("found")
        else:
            print("Not found")
print(checkforword)'''

'''def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(word in data):
            print("Found")
        else:
            print("Not found ")
check_for_word()'''

'''def check_for_word():
    word = "Javaa"
    data  = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no +=1
        else:
            print("Word does not exist")


check_for_word()
'''
#to count no of even number in the list
count = 0
with open("practice.txt","r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for val in nums:
        if(int(val) %2 == 0):
            count +=1

print(count)
