from Stmt import *

class Exp():
	pass


class Numeral(Exp):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
	def eval(self, state={}):
		return self.value


class Variable(Exp):
	def __init__(self, name):
		self.name = str(name)
	def __str__(self):
		return self.name
	def __repr__(self):
		return "Variable( %s )" % self.name
	def eval(self, state={}):
		return state.get(self.name)


class Sum(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s + %s" % (self.left, self.right)
	def __repr__(self):
		return "Adition( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)
		if(type(leftEval) != int): 
			raise Exception(repr(self) + " Bad left Sum value type") 
		
		rigthEval = self.right.eval(state)

		if(type(rigthEval) != int):
			raise Exception(repr(self) + " Bad right Sum value type") 

		return leftEval + rigthEval

class Mul(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s * %s" % (self.left, self.right)
	def __repr__(self):
		return "Multiplication( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)

		if(type(leftEval) != int): 
			raise Exception(repr(self) + " Bad left Mul value type") 
		
		rigthEval = self.right.eval(state)

		if(type(rigthEval) != int):
			raise Exception(repr(self) + " Bad right Mul value type") 

		return leftEval * rigthEval

class Diff(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s - %s" % (self.left, self.right)
	def __repr__(self):
		return "Difference( %s , %s )" % (repr(self.left),repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)

		if(type(leftEval) != int): 
			raise Exception(repr(self) + " Bad left Diff value type") 
		
		rigthEval = self.right.eval(state)

		if(type(rigthEval) != int):
			raise Exception(repr(self) + " Bad right Diff value type") 

		return leftEval - rigthEval


class TruthValue(Exp):
	def __init__(self,value):
		self.value = bool(value)
	def __str__(self):
		return str(self.value)
	def __repr__(self):
		return str(self.value)
	def eval(self, state={}):
		return self.value


class Equals(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s = %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "Equals( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)
		rigthEval = self.right.eval(state)

		if(type(leftEval) != type(rigthEval)): 
			raise Exception(repr(self) + " Incomparable types") 

		return leftEval == rigthEval

class Lte(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s <= %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "Lte( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)
		rigthEval = self.right.eval(state)

		if(type(leftEval) != type(rigthEval)): 
			raise Exception(repr(self) + " Incomparable types") 

		return leftEval <= rigthEval

class Not(Exp):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return "¬ (%s)" % str(self.value)
	def __repr__(self):
		return "Not( %s )" % repr(self.value)
	def eval(self, state={}):
		valueEval = self.value.eval(state)

		if(type(valueEval) != bool):
			raise Exception(repr(self) + " Incompatible type") 

		return not valueEval

class And(Exp):
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s ^ %s" % (str(self.left), str(self.right))
	def __repr__(self):
		return "And( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		leftEval = self.left.eval(state)
		rigthEval = self.right.eval(state)

		if(type(leftEval) != bool and type(rigthEval) != bool): 
			raise Exception(repr(self) + " Both value types must be bool") 

		return leftEval and rigthEval

class FunctionCall(Exp):
	def __init__(self, name, args):
		self.name = name
		self.args = args
	def __str__(self):
		return "FunctionCall %s (%s)" % (self.name, ",".join(self.args))
	def __repr__(self):
		return "FunctionCall( %s, %s )" % (repr(self.name), repr(self.args))
	def eval(self, state):
		function = state[self.name]
		if(type(function[1]) != Block):
			raise Exception(repr(self), "Variable is not a function")

		functionDefArgs = function[0]
		if(len(functionDefArgs) != len(self.args)):
			raise Exception(repr(self), "Invalid function arguments amount")
		argsEval = [x.eval(state) for x in self.args]
		namedArgs = dict(zip(functionDefArgs, argsEval))

		namedArgs['result'] = None
		print (namedArgs)
		functionBlock = function[1]

		functionBlock.eval(namedArgs)

		return namedArgs['result']
