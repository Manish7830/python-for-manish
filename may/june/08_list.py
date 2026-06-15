# Data structure
# data structure used to store data effeciently and make faster process
# for operations like read and write.


# 1. List : list()
# 2. String : str()
# 3. Dictionary : dict()
# 4. Set : set()
# 5. Tuple : tuple()



# 1. LIST
# 1.List is a data structure in python used to store multiple data in of different type in one variable.

# 2. List can define by using square [] and data inside known as element.

# 3. List can be hetrogenous and homogenous.

# 4. list are mutable (changeable)

# 5. list support indexing ,slicing and follows ordering sequnce.
    #  indexing is the position of the value
  # 0. List and its property
  # 1. Creation of list
  # 2. Updation of list
  # 3. Indexing 
  # 4. Slicing 
  # 5. Traversing / loop
  # 6. In-built methods
  # 7. Test
  # 8. Assigments


# marks_10th = [20,55,60,76,50,60] # under the list the name of data is element

# print(f"before update : {marks_10th}")

# marks_10th[0] = 200 #mutating list element using index.
# marks_10th[2] += 40
# marks_10th[1] *= 2
# marks_10th[3] //= 2
# marks_10th[4] -= 10
# marks_10th[5] /= 4
# print(f"after update : {marks_10th}")


# marks_10th = [20,55,60,76,50,60] # under the list the name of data is element

# print(f"before update : {marks_10th}")
# l = len(marks_10th)-1
# marks_10th[-l]
# print(marks_10th)




#   SLICING


# sub = [25,20,30,40,50,60,70,80,90]
# sub[4] = 100
# sub[3] = 55
# sub[2] = .001
# mark= sub[:5]
# print(mark)
# mark1 = sub[:len(sub)//2:-1]
# print(mark1)

### 6. Traversing

# sub = [25,20,30,35,40,45,50,55,60,70,80,90]
# for i in range(len(sub)):
#     if sub[i]%2==0:
#         print(f"even = {sub[i]}")
#     else:
#         print(f"odd = {sub[i]}")

# sub = [25,20,30,40,50,60,70,80,90]
# for i in range(len(sub)):
#     print(i)


# sub = [25,20,30,40,50,60,70,80,90]
# for i in sub:
#     if i%2==0:
#         print(f"this ele is even {i}")
#     else:
#         print(f"this ele is odd  {i}")


# sub = [25,20,30,40,50,60,70,80,90]
# total = 0
# for i in sub:
#     total += i
# print(total)




# sub = [25,20,30,40,90,85,80,75,70,65,60,50]

# sub.append(100)
# sub.append(105)
# sub.append(110)
# sub.sort()
# print(sub)




# var = [10,20,30,40,50,60,70,80,90,100,110,120,130,140]
# var1 = var[:5:-2]
# print(var1)


# IN-BUILD METHODS


#append

# emp_name=["aman","shivam"]
# new_emp="kamal"
# emp_name.append(new_emp)



# emp_list=["aman","shivam"]
# for i in range(1,11):
#     new_emp=input("Enter your name = ")
#     emp_list.append(new_emp)
# print(emp_list)



#extend


# emp_name=["aman","shivam"]
# print(emp_name)
# name_list=input("Enter name list = []")
# emp_name.extend(name_list)



#insert

emp_name=["aman","shivam"]
new_emp="kamal"
emp_name.insert(1,new_emp)





#-------=======pop=======--------
# default delete and return form  last otherwise specific index
# my_list=[100,111,200,620,320,300]
# print(my_list)
# d1=my_list.pop()
# d2=my_list.pop(1)

# print(my_list)
# print(d1,d2)


#***********====remove()=======************
#bydefault return nahi data
# default iss ma value dene padti ha
# my_list=[100,111,200,620,320,300]
# print(my_list)
# d1=my_list.remove(200)
# print(d1)

#+++++**+*+*+*+=8+*+*+8=*=8 clear =*=*=*=8+=*=(*)
# my_list=[100,111,200,620,320,300]
# my_list.clear
# print(my_list)





#==========reverse =====
# my_list=[100,111,200,620,320,300]
# my_list.reverse
# print(my_list)

# ---------------sort():- acending---------------

# my_list=[100,200,300,400,500,600,700,800,900]

# my_list.sort()

# print(my_list)

# ------------sort(reverce=true) decending-------------

# my_list=[100,200,300,400,500,600,700,800,900]
# my_list.sort(reverse=True)
# print(my_list)




#========copy===
# my_list=[100,111,200,620,320,300]
# my_list.copy
# print(my_list)

#=====index===
# my_list=[100,111,200,100,620,320,300]
# res=my_list.index
# print(my_list)
# print(res)


#======count=====
# my_list=[100,111,200,620,320,300]
# my_list.clear
# print(my_list)
# res=my_list.count(100)
# print(my_list)
# print(res)


# #====----universal-----
# my_list=[100,111,200,620,320,300]
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))



