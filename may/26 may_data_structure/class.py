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

# marks_10th = [20,55,60,76,50,60] # under the list the name of data is element

# print(f"before update : {marks_10th}")

# marks_10th[0] = 200 #mutating list element using index.
# marks_10th[2] += 40
# marks_10th[1] *= 2
# marks_10th[3] //= 2
# marks_10th[4] -= 10
# marks_10th[5] /= 4
# print(f"after update : {marks_10th}")


marks_10th = [20,55,60,76,50,60] # under the list the name of data is element

print(f"before update : {marks_10th}")
l = len(marks_10th)-1
marks_10th[-l]
print(marks_10th)
