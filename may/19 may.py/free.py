# var = input("enter you name = ")
# size = len(var) -1
# vowels = 0
# n = 0
# while n<=size:
#     if var[n] in "aeiou":
#         vowels +=1
#     n +=1
# print(vowels)            


# var = int(input("enter your number = "))
# n = 10
# i = 1
# while i <= n:
#     t = i*var
#     print(f"{var} x {i} = {t}")
#     i += 1


# def aver (a=0,b=0,c=0):
#     d = (a+b+c)/3
#     print(d)
#     return d
# aver(10,20,30,)  
#   


# def fact (a):
#     f = 1
#     for i in range(1,a+1):
#         f*=i
#     print(f)
# fact(int(input("enter your number = ")))

def val (a):
    if a%2==0:
        print ("even")

    else:
        print("odd")

val(20)