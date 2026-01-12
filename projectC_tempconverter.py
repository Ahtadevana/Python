#Making a temperature converter program
import sys #Solely used for sys.exit()

unit = input("What's the temperature unit you're using?(C/F): ").upper()
temp = float(input(f"What's the current temperature?(°{unit}): "))

def cel_to_fah(temp):
    return (temp * 9/5) + 32
def fah_to_cel(temp):
    return (temp - 32) * 5/9

if unit == "C":
    result = cel_to_fah(temp)
    out_unit = "°F"
elif unit == "F":
    result = fah_to_cel(temp)
    out_unit = "°C"
else:
    print(f'Your unit "{unit}" is INVALID! Unit must be C/F!')
    sys.exit() #Common use of exiting a program

print(f"---\nConverted successfully! Your result is: {result:.2f}{out_unit}")