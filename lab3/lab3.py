from fraction import Fraction

print('Welcome to Fun with Fractions!')

end = 0
while(end <=0):
  try:
    end = int(input("Enter Number of iterations (integer > 0): "))
    if(end <= 0):
      print("Invalid input!")
  except:
    print("Invalid input!")


def harmonicSeries(n):
  total = Fraction(0, 1)

  for i in range(1, n + 1):
    fraction = Fraction(1, i)
    total = total + fraction

  return total

def twoSeries(n):
  half = Fraction(1, 2)

  total = Fraction(0, 1)
  for i in range(0, n + 1):
    fraction = half ** i
    total = total + fraction

  return total

def zeroSeries(n):
  two = Fraction(2, 1)
  return two - twoSeries(n)

def partialRiemannZeta(n, b):
  total = Fraction(0, 1)

  for i in range(1, n + 1):
    fraction = Fraction(1, i) ** b
    total = total + fraction

  return total


harmonicResult = harmonicSeries(end)
twoResult = twoSeries(end)
zeroResult = zeroSeries(end)


print('H(' + str(end) +  ')=' + str(harmonicResult.num) + '/' + str(harmonicResult.den))
print('H(' + str(end) +  ')=~' + '%0.8F' % (harmonicResult.num / harmonicResult.den))

print('T(' + str(end) +  ')=' + str(twoResult.num) + '/' + str(twoResult.den))
print('T(' + str(end) +  ')=~' + '%0.8F' % (twoResult.num / twoResult.den))

print('Z(' + str(end) +  ')=' + str(zeroResult.num) + '/' + str(zeroResult.den))
print('Z(' + str(end) +  ')=~' + '%0.8F' % (zeroResult.num / zeroResult.den))

for b in range(2, 9):
  partialRiemannZetaResult = partialRiemannZeta(end, b)
  print('R(' + str(end) +  ',' + str(b) + ')=' + str(partialRiemannZetaResult.num) + '/' + str(partialRiemannZetaResult.den))
  print('R(' + str(end) +  ',' + str(b) + ')=~' + '%0.8F' % (partialRiemannZetaResult.num / partialRiemannZetaResult.den))
