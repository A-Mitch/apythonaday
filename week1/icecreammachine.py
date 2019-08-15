# It's hot outside so let's order some icecream

# The flavors
flavors = {'Vanilla': 3.50, 'Chocolate': 4.50, 'Pineapple': 5.50, 'Blueberry Rum': 6.50, 'Peach Soju Jam': 6.50}

# Prints the icecream
def printflavors():
    for k, v in flavors.iteritems():
        print(k + "   Price: "+str(v))

# Ask the user how much money they have
print("Welcome to Young Mitch's icecream shop. Here are our current selection of flavors: ")
printflavors()

# Get money amount from the user
useramnt = float(raw_input("Input your desired money credit amount: "))

if useramnt < 3.50:
    print("Sorry, we can't do anything with "+str(useramnt)+".")

userflav = raw_input("Which flavor would you like? ")
# Allows the user to purchase the icecream
def purchase(money):
    if userflav == "Vanilla":
        print("$ " + str(useramnt - 3.50))
    elif userflav == "Chocolate":
        print("$ " + str(useramnt - 4.50))
    elif userflav == "Pineapple":
        print("$ " + str(useramnt - 5.50))
    elif userflav == "Blueberry Rum":
        print("$ " + str(useramnt - 6.50))
    elif userflav == "Peach Soju Jam":
        print("$ " + str(useramnt - 6.50))

print("Great choice! I love that flavor! Your change is listed below: ")
purchase(useramnt)
print("Thank you and have a great day!")

    

