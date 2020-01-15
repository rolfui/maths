p = 0.01  # sannsynlighetn for hendelsen
k_start = 2  # P(X>=k-start) , stokastisk variabel
prob = 0.95  # P(X==k_start)>=prob
n = 400  # populasjon startverdi

def nCr(n,r):
   i=0
   prod=1
   while i<r:
      prod=prod*(n-i)/(i+1)
      i=i+1
   return prod

probCandidate=0
while probCandidate < prob:
   probCandidate = 0
   k = k_start
   while (k <= n):
      probCandidate = probCandidate + (nCr(n,k) * p**k * (1-p)**(n-k) )
      k = k+1
   print("n: " , n, " prob: ", probCandidate)
   n = n+1

print(nCr(34,7))