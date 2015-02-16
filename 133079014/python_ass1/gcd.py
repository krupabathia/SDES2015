def gcd(a,b):
	try:
		if (a < 0) or (b < 0):
			raise ValueError
		elif type(a) is not int:
			if type(a) is not long:
				raise TypeError
		elif type(b) is not int:
			if type(b) is not long:
				raise TypeError
		else:
			while b:
				a,b = b, a%b
			return a
	except ValueError:
		print "Both the numbers should be non-negative"
	except TypeError:
		print "Enter a number of valid type (positive integer or long)"
