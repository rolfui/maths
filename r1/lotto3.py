import numpy

myLine = set()
blWin = False
nTries = 0

#generate winning Lotto line
while len(myLine) < 7:
   number = numpy.random.randint(1,35)
   myLine.add(number)

#generate draw
while not  blWin:
   nTries = nTries + 1
   drawLine = set()
   while len(drawLine) < 7:
      number = numpy.random.randint(1,35)
      if number not in myLine:
         break
      drawLine.add(number)
   if len(drawLine) == 7:
      blWin = True


#myLine.sort()
#drawLine.sort()
myLine = list(myLine)
myLine.sort()
drawLine = list(drawLine)
drawLine.sort()
print("Min rekke:\t", myLine)
print("\nVinnerrekke:\t",drawLine)
print("\nVi vant etter " , nTries , " forsøk!")
