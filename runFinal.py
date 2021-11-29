
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from tabulate import tabulate
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
# Encoding that will store all of your constraints
E = Encoding()
############################################# Players

@proposition(E)
class p1Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1.{self.data}"
@constraint.at_most_one(E)
@proposition(E)
class p1State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1.{self.data}"
W_1 = p1Action("W") #Player 1 wins
D_1 = p1Action("D") #Player 1 has been damaged
P_1 = p1Action("P") #Player 1 performs a punch (range of 1 space)
K_1 = p1Action("K") #Player 1 performs a kick (range of 2 spaces)
T_1 = p1Action("T") #Player 1 performs a throw
B_1 = p1Action("B") #Player 1 is blocking
JUMP_1 = p1Action("JUMP") #Player 1 jumps
H_1 = p1Action("H") #Player 1 has performed a H (range of 3 spaces)
SHORYU_1 = p1Action("SHORYU") #Player 1 has performed a shoryuken (Beats MP)
p1ActionArray = [P_1,K_1,T_1,JUMP_1,H_1,SHORYU_1]

#
NEUTRAL_1 = p1State("NEUTRAL")#Player 1 is in a neutral positions
WHIFF_1 = p1State("WHIFF") #Player 1 whiffed their attack
@proposition(E)
class p2Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p2.{self.data}"
@constraint.at_most_one(E)
@proposition(E)
class p2State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p2.{self.data}"

#Propositions for player 2 
W_2 = p2Action("W") #Player 2 wins
D_2 = p2Action("D") #Player 2 has been damaged
P_2 = p2Action("P") #Player 2 performs a punch
K_2 = p2Action("K") #Player 2 performs a kick
T_2 = p2Action("T") #Player 2 performs a throw
B_2 = p2Action("B") #Player 2 is blocking
JUMP_2 = p2Action("JUMP") #Player 2 jumps
H_2 = p2Action("H") #Player 2 has performed a H
SHORYU_2 = p2Action("SHORYU") #Player 2 has performed a shoryuken
p2ActionArray = [P_2,K_2,T_2,JUMP_2,H_2,SHORYU_2]
#
NEUTRAL_2 = p2State("NEUTRAL")#Player 2 is in a neutral positions
WHIFF_2 = p2State("WHIFF") #Player 2 whiffed their attack
#Both
bothNeutral = (NEUTRAL_1&NEUTRAL_2)
############################################# Stage
@constraint.exactly_one(E)
@proposition(E)
class p1Position:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1Position.{self.data}"

@constraint.exactly_one(E)
@proposition(E)
class p2Position:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p2Position.{self.data}"

P1position = [0]*6
for i in range(6):
    P1position[i] = p1Position("SPACE_"+str(i))
P2position = [0]*6
for i in range(6):
    P2position[i] = p2Position("SPACE_"+str(i))
#Propositions pertaining to both players

fourSpacesBetween = ((P1position[0]&P2position[5])|(P1position[5]&P2position[0]))#In the first and last spots, also converse
threeSpacesBetween = ((P1position[0]&P2position[4])|(P1position[4]&P2position[0])|(P1position[1]&P2position[5])|(P1position[5]&P2position[1]))
twoSpacesBetween = ((P1position[0]&P2position[3])|(P1position[3]&P2position[0])|(P1position[1]&P2position[4])|(P1position[4]&P2position[1])|(P1position[2]&P2position[5])|(P1position[5]&P2position[2]))
oneSpaceBetween = ((P1position[0]&P2position[2])|(P1position[2]&P2position[0])|(P1position[1]&P2position[3])|(P1position[3]&P2position[1])|(P1position[2]&P2position[4])|(P1position[4]&P2position[2])|(P1position[3]&P2position[5])|(P1position[5]&P2position[3]))
#Adjacent would be 0 spaces away, right next to eachother
adjacent = ((P1position[0]&P2position[1])|(P1position[1]&P2position[2])|(P1position[2]&P2position[3])|(P1position[3]&P2position[4])|(P1position[4]&P2position[5])|(P1position[1]&P2position[0])|(P1position[2]&P2position[1])|(P1position[3]&P2position[2])|(P1position[4]&P2position[3])|(P1position[5]&P2position[4]))
#############################################

def game():
    #ATTACKS
    #throws
    E.add_constraint((B_1&T_2)&adjacent)#Throwing a blocking opponent works
    E.add_constraint((B_2&T_1)&adjacent)#Throwing a blocking opponent works
    E.add_constraint(T_2&adjacent)#Throwing an opponent works
    E.add_constraint(T_1&adjacent)#Throwing an opponent works
    #ATTACK RANGES
    E.add_constraint((P_1&~adjacent)>>(WHIFF_1))#If player 1 punches and player 2 is not adjacent then nothing happens
    E.add_constraint((P_2&~adjacent)>>(WHIFF_2))
    #throw Ranges
    E.add_constraint((P_1&~adjacent)>>(WHIFF_1))#If player 1 punches and player 2 is not adjacent then nothing happens
    E.add_constraint((P_2&~adjacent)>>(WHIFF_2))
    
    #DEFENCE
    E.add_constraint(H_1&JUMP_2)#Player 2 may jump to not get hit by a player 1 H
    E.add_constraint(H_2&JUMP_1)#The converse is also true
    #throw break
    E.add_constraint(((T_1&T_2)&(adjacent))>>bothNeutral)#Throw break
    #p1 blocking attacks
    for i in range(len(p2ActionArray)-1):
        E.add_constraint(p2ActionArray[i]&B_1)
    #p2 blocking attacks
    for i in range(len(p1ActionArray)-1):
        E.add_constraint(p1ActionArray[i]&B_2)
    #WIN CONDITIONS
    #player 1 gets hit
    for i in range(len(p2ActionArray)):
        E.add_constraint(p2ActionArray[i]&~B_1>>D_1)
    #player 2 gets hit
    for i in range(len(p1ActionArray)):
        E.add_constraint(p1ActionArray[i]&~B_2>>D_2)



    #Compiling and returning theory
    return E

if __name__ == "__main__":
    T = game()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    #print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())
    
    

    #print("\nVariable likelihoods for player 1:")
    #for v,vn in zip(p1ActionArray, 'abcxyz'):
        #print(" %s: %.2f" % (vn, likelihood(T, v)))
    #print("\nVariable likelihoods for player 2:")
    #for v,vn in zip(p2ActionArray, 'abcxyz'):
        #print(" %s: %.2f" % (vn, likelihood(T, v)))