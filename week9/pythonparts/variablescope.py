import builtins
# This is where I will be practicing variable scope

# Understanding variable scope in Python
# LEGB: Local, Enclosing, Global, Built-in

# Local: Variables defined in a fucntion
# Enclosing: Variables in the local scope of enclosing fucntions
# Global: Variables defined at the top of a module or declared using global var
# Built-in: Just pre-assigned names
# Python asks is the var is L->E->G->B

# Global and local scope (L and G)

world = 'Global'

def test(x):
    # we are now working with the global world var
    #global world 
    # Changing the world variable
    world = 'local var'
    print(x)

test('local x')
print(world)

# Built-in variables (B)
# Built-in are like keywords in java
low = min([6,4,22,9,1])
print(low)

# how to print all the built in keywords
# print(dir(builtins))

# Enclosing variables (E)
# Has to do with nested functions 
# Outer is the enclosing function

def outer():
    y = 'outer y' #local to outer function

    def inner():
        #allows us to work with Ls of Enclosing funcs
        # nonlocal y  
        y = 'inner y'  # local to inner function
        print(y)
    inner()
    print(y)

outer()

