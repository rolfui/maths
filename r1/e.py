import math


i=1
e=1
fact=1

while i<100000:
   fact=fact*i
   e=e+1/fact
   i=i+1
print(e)




#def factorial(n):
#   prod = 1
#   while n>0:
#      prod = prod * n
#      n = n-1
#   return prod
