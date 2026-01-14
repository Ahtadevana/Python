#Messing around with python string indexing
#[index start: end :: step]

phone_number = "1234-5678-9012-3456"
print(phone_number[5:])         #print the 5th index to the end
print(phone_number[:4])         #print the start until the 4th index
print(phone_number[10:14])      #print the 10th until the 14th index
print(phone_number[-1])         #print the last index
print(phone_number[-4:])        #print the last 4 indexes
print(phone_number[:-5])        #print the start and stops until the 5th from last character
print(phone_number[::2])        #prints every 2nd index (stepping)
print(phone_number[::3])        #print every 3rd index
print(phone_number[::-1])       #reverse the order of characters