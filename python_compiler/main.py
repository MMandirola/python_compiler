from Aexp import *
from Bexp import *
from Stmt import *


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

## While stmt test

print("*"*20)
print("While stmt test")
print("*"*20)

state = {}
contador = Variable("times")
assignation = Assign(contador, Numeral(10))

assignation.eval(state)

repeatCondition = Not(Lte(contador, Numeral(0)))
restar1 = Assign(contador, Diff(contador, Numeral(1)))
repeat = While(repeatCondition, restar1)
print(assignation)
print(repr(repeat))
repeat.eval(state)
assert contador.eval(state) == 0

print("*"*20)
print("Test passed, times = 0")
print("*"*20)
