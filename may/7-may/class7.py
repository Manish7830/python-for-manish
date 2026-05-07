# num = "aman"
# if num:
#     print(f"yes name {num} is provided")
#     add="noida"
#     if add:
#         print(f"yes add is : {add} provided")
#     else:
#         print(f"add is not provided")
# else:
#     print("not name is provided")



# num = 20
# if num%2==0:
#     print("even")
#     mob= input("enter your mobile number = ")
#     if mob==10:
#         print("va")
name = input("enter your name = ")
pre = int(input("enter your pre marks = "))
if pre>=400:
    print("your are pass in pre and eligble for mains")
    mains=int(input("enter your mains = "))
    if mains>=600:
        print("your are pass in mains and eligble for interviwe")
        inter=int(input("enter your interviwe marks = "))
        if inter>=700:
            print(f"you are selected as IAS Mr.{name}")
        else :
            print("you are fail in interviwe")
    else:
        print("fail in mains")
else :
    print("better luck next time , pre failed ")