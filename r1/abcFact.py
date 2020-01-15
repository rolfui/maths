from fractions import Fraction
import math

stra = input("a: ")
a = float(Fraction(stra))
strb = input("b: ")
b = float(Fraction(strb))
strc = input("c: ")
c = float(Fraction(strc))

strResult = ""
if a>0:
   if stra=="1": strResult += "x^2"
   else: strResult += stra + "x^2"
elif a<0:
   if stra=="-1": strResult += "-" + "x^2"
   else: strResult += stra + "x^2"
if b>0: strResult += "+" + strb + "x"
elif b<0: strResult += strb + "x"
if c>0: strResult += "+" + strc
elif c<0: strResult += strc

roots = []
signs = []

rootExp = b**2-4*a*c

if rootExp < 0:
   strResult += " kan ikke faktoriseres."
else :
   strResult += " = "
   if rootExp > 0:
      root = (-1 * b + math.sqrt(rootExp))/(2*a)
      roots.append(root)
      root = (-1 * b - math.sqrt(rootExp))/(2*a)
      roots.append(root)
   else:
      root = (-1 * b)/(2*a)
      roots.append(root)
      roots.append(root)
   for i in range(0,2):
      if roots[i] < 0: signs.append("(x+" + str(-1*roots[i]) + ")")
      elif roots[i] > 0: signs.append("(x-" + str(roots[i]) + ")");
      else: signs.append("x");
   strResult += str(a);
   for i in range(0,2):
      strResult += signs[i]

print(strResult)
