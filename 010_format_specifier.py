#Learning format specifiers and its properties

price = 1000.120
gpa = 3.41
temp = -15

print(f"Your total is $ {price:.2f}")  #only took 2 decimal portions
print(f"Your total is $ {price:10}")   #provide 10 character space for output (right alligned as default)

print(f"Your total is $ {price:+}")
print(f"Your total is {gpa:+}")
print(f"Your total is {temp:+}")    #display a positive or a negative value

print(f"Your total is:{price: }")
print(f"Your total is:{gpa: }")
print(f"Your total is:{temp: }")    #even out spaces for negative value variable

print(f"Your total is:{price:<10}")   #left adjustment
print(f"Your total is:{price:>10}")   #right adjustment (usually default)
print(f"Your total is:{price:^10}")   #center adjustment

print(f"Your total is:{price:,}")   #thousand separator replaced with commas

print(f"Your total is:{price:^10,.0f}") #you can also combine format specifiers together