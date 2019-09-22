# -*- coding: utf-8 -*-

n = 100
m = 4
k_min = 4
# m is unknown
r = 20

probCandidate = 0
prob = 0.294

def factorial(n):
   prod = 1
   while n>0:
      prod = prod * n
      n = n-1
   return prod

def nCr (n,r):
   return (factorial(n))/(factorial(r)*factorial(n-r))

while probCandidate <= prob:
   probCandidate = 0;
   k = k_min
   while k <= m:
      probCandidate = probCandidate + ( nCr(m,k) * nCr(n-m,r-k) ) / nCr(n,r)
      k = k+1
   print("m: " , m, " prob: ", probCandidate)
   m = m+1

