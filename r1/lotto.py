# -*- coding: utf-8 -*-

import numpy

winning = numpy.arange(1,35,1)
winning= numpy.random.choice(winning,7,replace=False)
winning.sort()
winning = list(winning)

i = 0;
blWin = False
while not blWin:
   candidate = numpy.arange(1,35,1)
   candidate = numpy.random.choice(candidate,7,replace=False)
   candidate.sort()
   candidate=list(candidate)
   i = i+1
#   print(i,": ",candidate)
   if candidate==winning:
      blWin = True

print("\nMin rekke: ", candidate)
print("\nVinnerrekke: ", winning)
print("\nAntall trekninger: ", i)
