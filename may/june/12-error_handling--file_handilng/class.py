# # error handling


# try:
#     n1=10
#     n2=2
#     res=n1/n2
#     print(res)
# except Exception as e:
#     print("Error : " , e)

# finally:
#     print("Thanks for visting...")






#     #   list  handling


# emp_list[]
# for i in range(1,11):
#     emp_list.append(i)
# print(emp_list)

# print([i**2 for i in range(1,11)])
# print([i for i in range(1,11) if i%2==0])
# print([str(i)+":EVEN" if i%2==0 else str(i)+":ODD" for i in range(1,11)])


# emp_name=["arvind","anuj","rohit"]
# res=[n.upper() for n in emp_name]
# res=["<->".joint(n) for n in emp_name]
# res=[n.lower() for n in emp_name]
# print(res)


fruits_list=["apple","mango","papaya","banana","orange","grapes"]
w=input("enter your words = ")
for i in fruits_list:
    if w in i:
        print(i)



res=[i.upper() for i in fruits_list if w in i]
print(res)

res=[i.upper() for i in fruits_list if w in i[0]]
print(res)