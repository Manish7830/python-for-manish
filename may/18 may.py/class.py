# var = input("enter you name = ")
# size = len(var) -1
# vowels = 0
# n = 0
# while n<=size:
#     if var[n] in "aeiou":
#         vowels +=1
#     n +=1
# print(vowels)            


var = int(input("enter your number = "))
n = 10
i = 1
while i <= n:
    t = i*var
    print(f"{var} x {i} = {t}")
    i += 1