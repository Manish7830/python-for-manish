n=int(input("enter your number 1 = "))
n1=int(input("enter your number 2 = "))
n2=int(input("enter your number 3 = "))
n3=int(input("enter your number 4 = "))
res=n>n1 and n2<n3
res1=n>=n1 or n2<=n3
res2=not(n==n1 or n2!=n3)
print(res)
print(res1)
print(res2)




n="rohit,manish,ajay,dev,iq,"
find=input("enter your name")
print(find in n)
print(find not in n)