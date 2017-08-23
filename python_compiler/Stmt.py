class Stmt():
	pass

class Semicolon(Stmt):
	def __init__(self,left,right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s ; %s" % ( str(self.left), str(self.right) )
	def __repr__(self):
		return "Semicolon( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		self.left.eval(state)
		self.right.eval(state)
		return state

class Asign(Stmt):
	def __init__(self,left,right):
		self.left = left
		self.right = right
	def __str__(self):
		return "%s := %s" % ( str(self.left), str(self.right) )
	def __repr__(self):
		return "Asign( %s, %s )" % (repr(self.left), repr(self.right))
	def eval(self, state={}):
		name = self.left.name
		state[name] = self.right.eval(state)
		return state

