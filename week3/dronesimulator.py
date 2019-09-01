# This program simulates flying drones doe my friend Juan who is too scared to fly his
# This program was created by Alexander Mitchell
# I'm actually really proud of this one. It's so cool!

commands = ["up","down","left","right","flip","current","commands","land","stop"]

def showcommands():
    com = ' ,'.join(map(str,commands))
    print(com)

# Start up the simulator
startup = input("Welcome to Drone Flight Navigator 3005! \n Did you want to start to flying? (Yes/No)  ").lower()
# print(startup)

# If they don't then exit the program else continue

if startup == "yes":
    print("Cool cool. Here are the commands: ")
    showcommands()
elif startup =="no":
    print("Okay that's fine... Bye.")
    exit()

update = input("Enter a command: ")
x = 1
y = 1

# This is for simulating flying the drone.
while update != "stop":
    update = input("Enter a command: ").lower()
    
    if update == "up":
        y +=1
        print("Ascending")
    elif update == "down":
        y -=1
        print("descending")
    elif update == "left":
        x -=1
        print("Going left")
    elif update == "right":
        x +=1
        print("Going right")
    elif update == "current":
        print("I am currently flying at X: "+str(x)+" Y: "+str(y))
    elif update == "commands":
        showcommands()
    elif update == "land":
        x=0
        y=0
        print("Descending to X: "+str(x)+" Y: "+str(y)+". Thanks for flying")
        exit()

  
