# -*- coding: utf-8 -*-

p = 0.80
k = 50
prob = 0.95
probCandidate = 0
n = k

def factorial(n):
   prod = 1
   while n>0:
      prod = prod * n
      n = n-1
   return prod

def nCr (n,r):
   return (factorial(n))/(factorial(r)*factorial(n-r))

while probCandidate < prob:
   probCandidate = 0;
   k = 50
   while (k <= n):
      probCandidate = probCandidate + ( nCr(n,k) * p**k * (1-p)**(n-k) )
      k = k+1
   print("n: " , n, " prob: ", probCandidate)
   n = n+1
