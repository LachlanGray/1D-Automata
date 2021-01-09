from automata import Automata
from matplotlib.pyplot import imshow, show

a = Automata(50,2)

g = a.play(100)

imshow(g)
show()