#accepting user input(Project ex. Madlibs, shopping cart)

def madlibs_game():
    mood = input("How are you feeling right now?: ")
    place = input("Where are you right now?: ")
    thing = input("What do you see right now?: ")

    print(f"You're feeling {mood}")
    print(f"You're currently at {place} then accidentally bump into {thing}")

def shopping_cart():
    item = input("What do you want to buy right now?: ")
    quantity = int(input("How many would you buy?: "))
    price = float(input("What would the price be?: "))

    total = quantity * price
    print(f"You're currently buying {quantity} {item}(s)")
    print(f"Your total would be ${total}")

shopping_cart()