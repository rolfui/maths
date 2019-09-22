import numpy

myLine = []
blWin = False
nTries = 0

#generate winning Lotto line
while len(myLine) < 7:
   number = numpy.random.randint(1,35)
   if number not in myLine:
      myLine.append(number)

#generate draw
while not blWin:
   blFinished = False
   nTries = nTries + 1
   drawLine = []
   score = 0
   while not blFinished:
      number = numpy.random.randint(1,35)
      if number not in drawLine:
         if number in myLine:
            drawLine.append(number)
            score = score + 1
            if score == 7:
               blWin = True
               blFinished = True
         else:
            blFinished = True


myLine.sort()
drawLine.sort()
print("\n\nVinnerrekke:\t",drawLine)
print("Min rekke:\t", myLine)
print("\nVi vant etter " , nTries , " forsøk!")
