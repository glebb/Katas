class FizzBuzzApp(object):
	def run(self, index):
		fb = FizzBuzz()
		values = ""
		for i in range(1, index + 1):
			values += fb.filter(i) + "\n"
		return values

class FizzBuzz(object):
    def filter(self, input):
		if input < 1:
			raise ValueError
		if self._isDivisableBy3(input) and self._isDivisableBy5(input):
			return "FizzBuzz"
		elif self._isDivisableBy3(input):
			return "Fizz"
		elif self._isDivisableBy5(input):
			return "Buzz"
		return str(input)

    def _isDivisableBy3(self, value):
		if value % 3 == 0:
			return True
		return False

    def _isDivisableBy5(self, value):
		if value % 5 == 0:
			return True
		return False

if __name__ == '__main__':
	fba = FizzBuzzApp()
	print fba.run(100)