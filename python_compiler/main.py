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

# If then stmt test

testMessage("If then else stmt test")

state = {}

toTest = Variable("toTest")
testPassed = Variable("testPassed")

assignation1 = Assign(toTest, Numeral(1))
assignation1.eval(state)

assignation2 = Assign(testPassed, TruthValue(False))
assignation2.eval(state)

condition = Equals(toTest, Numeral(1))

ifThen = IfThen(condition, Assign(testPassed, TruthValue(True)) )

print(assignation1)
print(repr(ifThen))

ifThen.eval(state)

assert testPassed.eval(state) == True

testMessage("Test passed, testPassed = True")

# Gte Test

state = {}

a = Variable("a")
b = Variable("b")

assignation1 = Assign(a, Numeral(1))
assignation1.eval(state)

assignation2 = Assign(b, Numeral(4))
assignation2.eval(state)

condition = Gte(a, b)

print(repr(condition))

assert condition.eval(state) == False

testMessage("Test passed, condition.eval(state) == False")
########################################

state = {}

a = Variable("a")
b = Variable("b")

assignation1 = Assign(a, Numeral(4))
assignation1.eval(state)

assignation2 = Assign(b, Numeral(1))
assignation2.eval(state)

condition = Gte(a, b)

print(repr(condition))

assert condition.eval(state) == True

testMessage("Test passed, condition.eval(state) == True")

#Division Test

a = Numeral(4)
b = Numeral(2)
division = Division(a,b)

print (repr(division))
assert division.eval(state) == 2

testMessage("Test passed, division.eval(state) == 2")
########################################
state = {}
a = Numeral(4)
b = Numeral(0)
division = Division(a,b)

print (repr(division))

try:
	division.eval(state)
except Exception:
	testMessage("Test passed, NO division by zero")
