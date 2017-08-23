from Aexp import *
from Bexp import *
from Stmt import *


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

