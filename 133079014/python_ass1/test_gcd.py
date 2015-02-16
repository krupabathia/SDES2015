from gcd import gcd
def test_bothnegative():
	gcd(-1,-2)

'''if __name__ == '__main__':
	test_bothnegative()
'''
	
def test_bothpositive():
	assert gcd(12,18) == 6
	assert gcd(0,7) == 7

def test_onenegative():
	gcd(12,-18)

def test_string():
	gcd(1,'a')
	
test_bothpositive()
test_onenegative()
test_bothpositive()
test_string()
	
