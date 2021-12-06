from tabulate import tabulate


#list1 = [['a','b','c'],['d','e','f'],['g','h','i']]

#print(tabulate(list1))

#propValueTable = [[],[]]#First row will be proposition names, second will be their truth values

# import module
from tabulate import tabulate
  
# assign data
mydata = [{"a","b","c","d   "}]
  
# create header
head = ["Player 1 attack", "Player 2 attack", "Player 1 position", "Player 2 position"]
  
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))