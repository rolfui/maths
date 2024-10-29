from fractions import Fraction

stra = input("a: ")
a = float(Fraction(stra))
strb = input("b: ")
b = float(Fraction(strb))
strc = input("c: ")
c = float(Fraction(strc))

strResult = "(" + stra + "x^2) + (" + strb + "x) + (" + strc + ") = 0  har "
rootExp = b**2 - 4*a*c


if rootExp < 0:
   strResult += "ingen løsninger"
elif rootExp >0:
   strResult += "to løsninger"
else:
   strResult += "en løsning"

print(strResult)
