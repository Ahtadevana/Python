#making a compound interest calculator

principle = float(input("Insert the amount you started with: "))

while principle < 0:
    print("Amount must be equal or above than zero")
    principle = float(input("Insert the amount you started with: "))
rate = float(input("Insert the annual interest rate: "))

while rate < 0:
    print("Interest rate must be equal or above than zero")
    rate = float(input("Insert the annual interest rate: "))
years = int(input("Insert how long the money is saved in year(s): "))

while years < 0:
    print("Year must be equal or above than zero")
    years = int(input("Insert how long the money is saved in year(s): "))

result = principle * pow((1 + rate/100), years) #either pow or ** is both the same
print(f"Result: ${result:,.2f}")