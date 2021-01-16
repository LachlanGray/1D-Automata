from automata import Automata
from matplotlib.pyplot import imshow, show

a = Automata(100,3)

g = a.maj_rule(100)

print(g)