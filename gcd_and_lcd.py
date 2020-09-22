def gcd(divisor, dividend):
	remainder = None
	while (remainder != 0):
		remainder = dividend % divisor
		dividend = divisor
		divisor = remainder
	return dividend


def lcd(num1, num2):
	lcd_num = num1 * num2
	lcd = lcd_num / gcd
	return lcd


print("Greatest Common Divisor and Lowest Common Divisor Calculator:")

num1 = int(input("input first number: "))
num2 = int(input("input second number: "))
divisor = num1
dividend = num2
gcd = gcd(divisor, dividend)
lcd = lcd(num1, num2)
print("GCD = %i" % gcd)
print("LCD = %i" % lcd)