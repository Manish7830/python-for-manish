# var = [10,20,30,40,50,60,70,80,90,100,110,120,130,140]
# var1 = var[:5:-2]
# print(var1)

# wap to swap the first value of list with last value of list.

# var = [10,20,30,40,50,60,70,80]
# v1 = var[0]
# var[0] = var[-1]
# var[-1] = v1
# print(var)

#wap to find sum of the all elment in the list : [10,20,30,40,50]
 
# list = [10,20,30,40,50]
# s = 0
# for i in list:
#     s += i
# print(s)

# sum of only even elment 
# var = [10,3,4,6,22,31,55,40]
# s = 0
# for i in var :
#     if i%2 ==0:
#         s += i
# print(s)


#sum of odd
# var = [10,3,4,6,22,31,55,40]
# s = 0
# for i in var :
#     if i%2 !=0:
#         s += i
# print(s)


# how many int value and str value in the list
list = [12,10,"how",20,52,"python",25,32,"by",31,33,"hello"]
iv = 0
s = 0
o = 0
for i in list:
    if type(i) == str:
        iv += 1
        
    elif type(i) == int:
        s += 1
    else:
        o += 1
print(f"int value = {iv} , str value = {s} , other value = {o}")
