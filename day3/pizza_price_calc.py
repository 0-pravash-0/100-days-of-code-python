print("Welcome to Python Pizza Deliveries!") 

size = input("What size pizza do you want? S, M or L: ") 

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ") 

extra_cheese = input("Do you want extra cheese? Y or N: ") 

price = 0
#todo: work out how much they need to pay based on their size choice. 

if size == "S":
    price = 15

elif size =="M":
    price = 20

elif size == "L":
    price = 25

# todo: work out how much to add to their bill based on their pepperoni choice. 

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price +=3
    

# todo: work out their final amount based on whether if they want extra cheese.

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}")
