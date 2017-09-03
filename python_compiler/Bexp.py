class Bexp():
	pass


class TruthValue(Bexp):
	def __init__(self,value):
		self.value = bool(value)
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
	def eval(self, state={}):
		return self.value


class Equals(Bexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s = %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "Equals( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) == self.right.eval(state)


class Lte(Bexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s <= %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "Lte( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) <= self.right.eval(state)

class Gte(Bexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s >= %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "Gte( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) >= self.right.eval(state)

class Not(Bexp):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "¬ (%s)" % str(self.value)
	def __repr__(self):
		return "Not( %s )" % repr(self.value)
	def eval(self, state={}):
		return  not self.value.eval(state)

class And(Bexp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s ^ %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "And( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		return self.left.eval(state) and self.right.eval(state)


