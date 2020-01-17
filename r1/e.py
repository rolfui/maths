import math


i=1
e=1  #0!
fact=1  #0!

while i<3:
   fact=fact*i
   e=e+1/fact
   print(i,e)
   i=i+1




#def factorial(n):
#   prod = 1
#   while n>0:
#      prod = prod * n
#      n = n-1
#   return prod
