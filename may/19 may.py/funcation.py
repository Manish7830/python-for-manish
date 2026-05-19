# what is funcation.
# 1. Every funcation has their own purpose.
# 2. Funcation is block of insturction (code) which execute its oun block.
# 3. Funcation is reusable means define one time use manytime (DRY).
# 4. Fuuncation has two main part first funcation defination second funcation calling.

# how define funcation in python
# def add():  # () this is the perameter
#     a = 21
#     b = 10
#     c = a + b
#     print(c)
# add()    # () this is the arguments

# funcation divide into 4 category.
# 1. Take nothing return nuthing
# 1. Take nothing return something.
# 3. take somthing return nothing.
# 4. take somthing return somthing.


#parameters (para) and arguments (argu)
# positional parameter/arguments


# def add(a,b):
#     c = a+b
#     print(c)

# add(25,30)    

# def add(a,b,c):
#     d = a+b+c
#     print(d)
# add(25,30,50)    


# def table(n):
#     for i in range(1,11):
#         print(f"{n} x {i} = {i*n}")

# table(25)
# print()
# table(20)
# print("-"*20)
# table(30)


#default parameter
# def add(a=0,b=0,c=0):
#     print(a+b+c)

# add(20,10)

def multi(a=1,b=1):
    print(a*b)
multi(10,30)

def divi(a=1,b=1):
    print(a//b)
divi(10,5)

def sub(a=0,b=0):
    print("sub:"a-b)
sub(20,10)

def pow(a=1,b=1):
    print("power: "a**b)
pow(5,2)

def add(a=0,b=0,c=0):
    print("add: "a+b+c)
add(10,20,30)    
