# vowel count


# def string(str):
#     c = 0
#     for i in str:
#         if i in "aeiouAEIOU":
#             c += 1
#     return c

# res = string(input("enter your string = "))
# print(f"vowel in string is {res}")


# def add(a):
#     v=0
#     for i in a:
#         if i in "aeiouAEIOU":
#             v+=1
#     return v

# res = add(input("enter your string = "))

# print(res)        /





# Local variable vs global variable
# local var is used to global var




# # Global
# def msg():
#     global name
#     name = "manish"
#     print(name)
# msg()

# print(name)    



# # Local
# def msg():
#     name = "manish"
#     print(name)
# msg()

# print(name) 



# waf to count char "p" in "python programming"

# def add(a):
#     c = 0
#     for i in a:
#         if i in "p":
#             c += 1
#     return c 
# text = input("enter your string = ")
# res = add(text)
# print (res)      


# def add(a):
#     c = 0
#     for i in a:
#         if i in "o":
#             c += 1
#     return c 
# text = input("enter your string = ")
# res = add(text)
# print (res)     


# def vowel(dest,find):
#     c = 0
#     for i in dest:
#         if i == find:
#             c += 1
#     return c
# dest = "python programming"
# find = "p"
# res = vowel(dest,find)



# waf to sum of strings indexes
# def str(a):
#     s = 0
#     for i in len(a):
#         s += 1
#     return s

# text = "python"
# res = str(text)
# print(res)


def add (a):
    s = 0
    size = len(a)
    for i in range(size):
        s += i
    return s
sum = add("python")
print(sum)