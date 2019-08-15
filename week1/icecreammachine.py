# Created and done by Alexander Mitchell
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

    if (userflav == "Vanilla") and (str(useramnt) >= str(3.50)):
        print("Classic, safe. I like your style. Your change is listed below: ")
        print("$ " + str(useramnt - 3.50))
    
    if (userflav == "Chocolate") and (useramnt >= 4.50):
        print("It's cool. Your change is listed below: ")
        print("$ " + str(useramnt - 4.50))
    elif (useramnt < 4.50):
        print("not enough")
        exit()
    
    if (userflav == "Pineapple") and (useramnt >= 5.50):
        print("And on the eighth day Yeezus made this. Your change is listed below: ")
        print("$ " + str(useramnt - 5.50))
    elif (useramnt < 5.50):
        print("not enough")
        exit()
    
    if (userflav == "Blueberry Rum") and (useramnt >= 6.50):
        print("Friggin amazing! Your change is listed below: ")
        print("$ " + str(useramnt - 6.50))
    elif (useramnt < 6.50):
        print("not enough")
        exit()

    if (userflav == "Peach Soju Jam") and (useramnt >= 6.50):
        print("This is delicious, you will love it. Your change is listed below: ")
        print("$ " + str(useramnt - 6.50))
    elif (useramnt < 6.50):
        print("not enough")
        exit()
    
    if(userflav == "Yeet") and (useramnt > 100):
        print("You found the secret yeet flavor. You will be blessed beyond your wildest dreams")
    elif (userflav != "Yeet") and (useramnt < 100):
        print("A thousand years of curses for you")
    

purchase(useramnt)
print("Thank you and have a great day!")

    

