from Aexp import *
from Bexp import *
from Stmt import *
from utils import *

'''
tres = Numeral(3)
dos = Numeral(2)
suma = Sum(tres,dos)
uno = Numeral(1)
cuatro = Numeral(4)
suma2 = Sum(uno,cuatro)
igual = Equals(suma, suma2)
notigual = Not(igual)
print(repr(igual))
print(igual)
print(igual.eval())
print(repr(notigual))
print(notigual)
print(notigual.eval())
'''

# If then else stmt test

testMessage("If then else stmt test")

state = {}

toTest = Variable("toTest")
testPassed = Variable("testPassed")

assignation1 = Assign(toTest, Numeral(1))
assignation1.eval(state)

assignation2 = Assign(testPassed, TruthValue(False))
assignation2.eval(state)

condition = Equals(toTest, Numeral(1))

ifThenElse = IfThenElse(condition, Assign(testPassed, TruthValue(True)), Assign(testPassed, TruthValue(False)))

print(assignation1)
print(repr(ifThenElse))

ifThenElse.eval(state)

assert testPassed.eval(state) == True

testMessage("Test passed, testPassed = True")

# While stmt test

testMessage("While stmt test")

state = {}

contador = Variable("times")
assignation = Assign(contador, Numeral(10))
assignation.eval(state)

repeatCondition = Not(Lte(contador, Numeral(0)))

diff1 = Assign(contador, Diff(contador, Numeral(1)))

repeat = While(repeatCondition, diff1)

print(assignation)
print(repr(repeat))
repeat.eval(state)

assert contador.eval(state) == 0

testMessage("Test passed, times = 0")
