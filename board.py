
from bauhaus import Encoding, proposition, constraint
from bauhaus.core import print_theory
from bauhaus.utils import count_solutions, likelihood
from tabulate import tabulate

BGMAP = {
    'orange': 'orange_1',
    'pink': 'pink_1',
    'blue': 'blue',
    'green': 'light_green',
    'yellow': 'light_yellow',
    'red': 'red'
}

import pprint
import itertools
from run import flawlessDefence
import run

D = flawlessDefence()
D = D.compile()

alist = []
for key,value in D.solve().items():
    if value == True:
        print(key)
        alist.append(key)

# for i in range(2):
#     print(type(alist[i]))
#     if isinstance(alist[i], run.p2Action):
#         if doing this, have to add the data value to mydata somehow

  
# Add .data or .position manually in column according to where it should go
mydata = [[alist[1].data + ", " + alist[4].data, alist[0].data + ", " + alist[5].data, alist[3].position,alist[2].position]]

# create header
head = ["Player attack", "Player defense", "Player 1 position", "Player 2 position"]
  
# display table
print(tabulate(mydata, head, tablefmt="fancy_grid"))