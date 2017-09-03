#from Aexp import *
#from Bexp import *
from Stmt import *
from utils import *
from Exp import *


### If then else stmt test

state = {}

testMessage(state, "If then else stmt test")

toTest = Variable("toTest")
testPassed = Variable("testPassed")

assignation1 = Assign(toTest, Numeral(1))
assignation1.eval(state)

assignation2 = Assign(testPassed, TruthValue(False))
assignation2.eval(state)

condition = Equals(toTest, Numeral(1))

ifThenElse = IfThenElse(condition, Block([Assign(testPassed, TruthValue(True))]), Block([Assign(testPassed, TruthValue(False))]))

print(assignation1)
print(repr(ifThenElse))

ifThenElse.eval(state)

assert testPassed.eval(state) == True

testMessage(state, "Test passed, testPassed = True")



### While stmt test

state = {}

testMessage(state, "While stmt test")

contador = Variable("times")
assignation = Assign(contador, Numeral(10))
assignation.eval(state)

repeatCondition = Not(Lte(contador, Numeral(0)))

whileBlock = Block([Assign(contador, Diff(contador, Numeral(1)))])

repeat = While(repeatCondition, whileBlock)

print(assignation)
print(repr(repeat))
repeat.eval(state)

assert contador.eval(state) == 0

testMessage(state, "Test passed, times = 0")



### Fib test with temp variable new block scope

state = {}

testMessage(state, "Fib test with temp variable new block scope")

a = Variable("a")
b = Variable("b")
n = Variable("n")

assignation = Assign(a, Numeral(0))
assignation.eval(state)

assignation = Assign(b, Numeral(1))
assignation.eval(state)

assignation = Assign(n, Numeral(10))
assignation.eval(state)


repeatCondition = Not(Lte(n, Numeral(1)))
diff = Assign(n, Diff(n, Numeral(1)))
copyTemp = Assign(Variable("temp"), a)
swap = Assign(a, b)
calculus = Assign(b, Sum(Variable("temp"), b))

whileBlock = Block([copyTemp, swap, calculus, diff])
repeat = While(repeatCondition, whileBlock)

print(repr(repeat))
repeat.eval(state)

assert b.eval(state) == 55

testMessage(state, "Test passed, Fib = 55")



### Fib test function

state = {}

testMessage(state, "Fib test function")

# 
n = Variable("n")

assignation = Assign(n, Numeral(10))
assignation.eval(state)


a = Variable("a")
b = Variable("result")
cant = Variable("n")

assignationa = Assign(a, Numeral(0))
assignation.eval(state)

assignationb = Assign(b, Numeral(1))
assignation.eval(state)




repeatCondition = Not(Lte(cant, Numeral(1)))
diff = Assign(cant, Diff(cant, Numeral(1)))
copyTemp = Assign(Variable("temp"), a)
swap = Assign(a, b)
calculus = Assign(b, Sum(Variable("temp"), b))

whileBlock = Block([copyTemp, swap, calculus, diff])
repeat = While(repeatCondition, whileBlock)

fibFunction = FunctionDef("fib", ["n"], Block([assignationa, assignationb, repeat]))
fibFunction.eval(state)

fibFunctionCall = FunctionCall("fib", [n])

print(fibFunction)

assert fibFunctionCall.eval(state) == 55

testMessage(state, "Test passed, Fib = 55")
