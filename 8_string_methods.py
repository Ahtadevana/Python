#Making a name check requirements using string methods
#Name must not exceed 12 characters, must not contain spaces and numbers

name = input("What's your name?: ")

if len(name) > 12:
    print("Name must NOT exceed 12 characters")
elif name.find(" ") != -1:  #-1 means the .find() doesnt find space. But if it did, it runs this
    print("Name must NOT contain spaces")
elif not name.isalpha():
    print("Name must NOT contain numbers")
else:
    print("Access Granted!")
