#Simple Calculator Program
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

first_num = float(input("Input the first number: "))
second_num = float(input("Input the second number: "))
print("\n-----")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

choice = int(input("What would you like to do?: "))
if choice == 1:
    total = add(first_num, second_num)
elif choice == 2:
    total = subtract(first_num, second_num)
elif choice == 3:
    total = multiply(first_num, second_num)
elif choice == 4:
    total = divide(first_num, second_num)
else:
    print("Invalid Choice!")

print(round(total))