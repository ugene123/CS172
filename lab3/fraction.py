class Fraction:

	#Constructor. Puts fraction in simplest form
	def __init__(self, a, b):
		self.num = a
		self.den = b
		self.simplify()

	#Print Fraction as a String
	def __str__(self):
		if(self.den == 1):
			return str(self.num)
		else:
			return str(self.num)+"/"+str(self.den)

	#Get the Numerator
	def getNum(self):
		return self.num

	#Get the Denominator
	def getDen(self):
		return self.den

	#Give Numerical Approximation of Fraction
	def approximate(self):
		return self.num/self.den

	#Simplify fraction
	def simplify(self):
		x = self.gcd(self.num,self.den)
		self.num = self.num // x
		self.den = self.den // x

	#Find the GCD of a and b
	def gcd(self, a, b):
		if(b == 0):
			return a
		else:
			return self.gcd(b, a % b)

	def __add__(self, other):
		a = self.num * other.den + other.num * self.den
		b = self.den * other.den
		result = Fraction(a, b)
		return result

	def __sub__(self, other):
		other.num = other.num * -1 
		result = self + other
		return result

	def __mul__(self, other):
		a = self.num * other.num
		b = self.den * other.den 
		result = Fraction(a, b)
		return result 

	def __truediv__(self, other):
		num = other.num
		den = other.den
		other.num = den
		other.den = num
		result = self * other
		return result


	# (1/2) ^ 3 = 1/8
	def __pow__(self, exp):
		if(exp == 0):
			return Fraction(1, 1)

		if(exp < 0):
			positiveExp = exp * -1
			flipped = Fraction(self.den, self.num)
			flipped ** positiveExp

		if(exp == 1):
			return self

		if(exp > 1):
			product = Fraction(1,1)
			for i in range(exp):
				product = self * product

			return product

