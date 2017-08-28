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

class Assign(Stmt):
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

class IfThenElse(Stmt):
	def __init__(self, condition, ifBody, elseBody):
		self.condition = condition
		self.ifBody = ifBody
		self.elseBody = elseBody
	def __str__(self):
		return "if %s then %s else %s" %(str(self.condition), str(self.ifBody), str(self.elseBody))
	def __repr__(self):
		return "If( %s, %s, %s)" %(str(self.condition), str(self.ifBody), str(self.elseBody))
	def eval(self, state={}):
		if self.condition.eval(state): 
			self.ifBody.eval(state) 
		else:
			self.elseBody.eval(state) 

class While(Stmt):
	def __init__(self, condition, whileBody):
		self.condition = condition
		self.whileBody = whileBody
	def __str__(self):
		return "while %s do %s" %(str(self.condition), str(self.whileBody))
	def __repr__(self):
		return "While( %s, %s )" %(str(self.condition), str(self.whileBody))
	def eval(self, state={}):
		while self.condition.eval(state): 
			self.whileBody.eval(state)


