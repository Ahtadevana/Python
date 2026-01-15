divider = "------------"

for i in range(1, 11):
    print(i)    #prints 1-10 on a new line
print(divider)

for i in reversed(range(1, 11)):
    print(i)    #prints 10 to 1 on a new line (reversed)
print(divider)

phone_number = "1234-5678-9012"
for i in phone_number:
    print(i)
print(divider)

for i in range(1,21):
    if i == 4:
        continue    #the loop skips over number "4"
    elif i == 13:
        break       #the loop stops after number "13"
    print(i)
