# -*- coding: utf-8 -*-

import numpy

winning = []
blWin = False
nTries = 0

while len(winning) < 7:
   number = numpy.random.randint(1,35)
   if number not in winning:
      winning.append(number)

while not blWin:
   blFinished = False
   nTries = nTries + 1
   candidate = []
   score = 0
   while not blFinished:
      number = numpy.random.randint(1,35)
      if number not in candidate:
         if number in winning:
            candidate.append(number)
            score = score + 1
            if score == 7:
               blWin = True
               blFinished = True
         else:
            blFinished = True


winning.sort()
candidate.sort()
print("\n\nVinnerrekke:\t",winning)
print("Vår rekke:\t", candidate)
print("\nVi vant etter " , nTries , " forsøk!")
