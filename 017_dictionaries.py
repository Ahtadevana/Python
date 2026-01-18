spaces = "--------------------"
databank = {"feline": "cat",
            "poultry": "chicken",
            "vegetables": "broccoli",
            "fruit": "watermelon",}

print(databank.items())
print(spaces)

for data in databank:
    print(data)
print(spaces)

print(databank.keys())
print(spaces)

print(databank.values())
print(spaces)