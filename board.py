from tabulate import tabulate
from StageProps import*
from PlayerProps import*
list1 = [['a','b','c'],['d','e','f'],['g','h','i']]

print(tabulate(list1))

propValueTable = [[],[]]#First row will be proposition names, second will be their truth values
