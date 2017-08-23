class Aexp():
	pass


class Numeral(Aexp):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
	def eval(self, state={}):
		return self.value


class Variable(Aexp):
	def __init__(self, name):
		self.name = str(name)
	def __str__(self):
		return self.name
	def __repr__(self):
		return "Variable( %s )" % self.name
	def eval(self, state={}):
		return state.get(self.name)


class Sum(Aexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s + %s" % (self.left, self.right)
	def __repr__(self):
		return "Adition( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) + self.right.eval(state)

class Mul(Aexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s * %s" % (self.left, self.right)
	def __repr__(self):
		return "Multiplication( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) * self.right.eval(state)

class Diff(Aexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s - %s" % (self.left, self.right)
	def __repr__(self):
		return "Difference( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) - self.right.eval(state)