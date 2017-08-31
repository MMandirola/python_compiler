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
		state[self.left.name] = self.right.eval(state)

class IfThenElse(Stmt):
	def __init__(self, condition, ifBlock, elseBlock):
		self.condition = condition
		self.ifBlock = ifBlock
		self.elseBlock = elseBlock
	def __str__(self):
		return "if %s then %s else %s" %(str(self.condition), str(self.ifBlock), str(self.elseBlock))
	def __repr__(self):
		return "If( %s, %s, %s)" %(str(self.condition), str(self.ifBlock), str(self.elseBlock))
	def eval(self, state={}):
		if self.condition.eval(state): 
			self.ifBlock.eval(state) 
		else:
			self.elseBlock.eval(state) 

class While(Stmt):
	def __init__(self, condition, whileBlock):
		self.condition = condition
		self.whileBlock = whileBlock
	def __str__(self):
		return "while %s do %s" %(str(self.condition), str(self.whileBlock))
	def __repr__(self):
		return "While( %s, %s )" %(str(self.condition), str(self.whileBlock))
	def eval(self, state={}):
		while self.condition.eval(state): 
			self.whileBlock.eval(state)

class Block(Stmt):
	def __init__(self, stmts):
		self.stmts = stmts
	def __str__(self):
		return "Block %s" %(",".join(map(str, self.stmts)))
	def __repr__(self):
		return "Block( %s )" %(",".join(map(repr, self.stmts)))
	def eval(self, state={}):
		stateCopy = state.copy()

		for stm in self.stmts:
			stm.eval(stateCopy)

		oldKeys = filter(lambda x: x[0] in state.keys(), stateCopy.items())

		state.update(dict(oldKeys))

class FunctionDef(Stmt):
	def __init__(self, name, args, block):
		self.name = name
		self.args = args
		self.block = block 
	def __str__(self):
		return "Function %s (%s) %s" %(self.name, ",".join(self.args), self.block)
	def __repr__(self):
		return "Function (%s , %s , %s )" %(self.name, ",".join(map(repr, self.args)), repr(self.block))
	def eval(self, state={}):
		state[self.name] = (self.args, self.block)
