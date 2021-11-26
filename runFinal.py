
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
# Encoding that will store all of your constraints
E = Encoding()
############################################# Players
@constraint.at_most_one(E)
@proposition(E)
class p1Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"
@constraint.at_most_one(E)
@proposition(E)
class p1State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"
W_1 = p1Action("W_1") #Player 1 wins
D_1 = p1Action("D_1") #Player 1 has been damaged
P_1 = p1Action("P_1") #Player 1 performs a punch (range of 1 space)
K_1 = p1Action("K_1") #Player 1 performs a kick (range of 2 spaces)
T_1 = p1Action("T_1") #Player 1 performs a throw
B_1 = p1Action("B_1") #Player 1 is blocking
JUMP_1 = p1Action("JUMP_1") #Player 1 jumps
H_1 = p1Action("H_1") #Player 1 has performed a H (range of 3 spaces)
SHORYU_1 = p1Action("SHORYU_1") #Player 1 has performed a shoryuken (Beats MP)
#
NEUTRAL_1 = p1State("NEUTRAL_1")#Player 1 is in a neutral positions
WHIFF_1 = p1State("WHIFF_1") #Player 1 whiffed their attack

@constraint.at_most_one(E)
@proposition(E)
class p2Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"
@constraint.at_most_one(E)
@proposition(E)
class p2State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"

#Propositions for player 2 
W_2 = p2Action("W_2") #Player 2 wins
D_2 = p2Action("D_2") #Player 2 has been damaged
P_2 = p2Action("P_2") #Player 2 performs a punch
K_2 = p2Action("K_2") #Player 2 performs a kick
T_2 = p2Action("T_2") #Player 2 performs a throw
B_2 = p2Action("B_2") #Player 2 is blocking
JUMP_2 = p2Action("JUMP_2") #Player 2 jumps
H_2 = p2Action("H_2") #Player 2 has performed a H
SHORYU_2 = p2Action("SHORYU_2") #Player 2 has performed a shoryuken
#
NEUTRAL_2 = p2State("NEUTRAL_2")#Player 2 is in a neutral positions
WHIFF_2 = p2State("WHIFF_2") #Player 2 whiffed their attack
#Both
bothNeutral = (NEUTRAL_1&NEUTRAL_2)
############################################# Stage
@constraint.exactly_one(E)
@proposition(E)
class p1Position:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"

@constraint.exactly_one(E)
@proposition(E)
class p2Position:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"A.{self.data}"

P1position = [0]*6
for i in range(6):
    P1position[i] = p1Position("SPACE_1_"+str(i))
P2position = [0]*6
for i in range(6):
    P2position[i] = p2Position("SPACE_2_"+str(i))
#Propositions pertaining to both players

fourSpacesBetween = ((P1position[0]&P2position[5])|(P1position[5]&P2position[0]))#In the first and last spots, also converse
threeSpacesBetween = ((P1position[0]&P2position[4])|(P1position[4]&P2position[0])|(P1position[1]&P2position[5])|(P1position[5]&P2position[1]))
twoSpacesBetween = ((P1position[0]&P2position[3])|(P1position[3]&P2position[0])|(P1position[1]&P2position[4])|(P1position[4]&P2position[1])|(P1position[2]&P2position[5])|(P1position[5]&P2position[2]))
oneSpaceBetween = ((P1position[0]&P2position[2])|(P1position[2]&P2position[0])|(P1position[1]&P2position[3])|(P1position[3]&P2position[1])|(P1position[2]&P2position[4])|(P1position[4]&P2position[2])|(P1position[3]&P2position[5])|(P1position[5]&P2position[3]))
#Adjacent would be 0 spaces away, right next to eachother
adjacent = ((P1position[0]&P2position[1])|(P1position[1]&P2position[2])|(P1position[2]&P2position[3])|(P1position[3]&P2position[4])|(P1position[4]&P2position[5])|(P1position[1]&P2position[0])|(P1position[2]&P2position[1])|(P1position[3]&P2position[2])|(P1position[4]&P2position[3])|(P1position[5]&P2position[4]))
#############################################

def game():
    #Defence options
    E.add_constraint(H_1&JUMP_2)#Player 2 may jump to not get hit by a player 1 H
    E.add_constraint(H_2&JUMP_1)#The converse is also true
    #Throws
    E.add_constraint(((T_1&T_2)&(adjacent))>>bothNeutral)#Throw break
    E.add_constraint(((B_1)&(T_2))&adjacent)#Throwing a blocking opponent works
    E.add_constraint(((B_1)&(T_2))&adjacent)#Throwing a blocking opponent works
    #Attack Ranges
    E.add_constraint((P_1&~adjacent)>>(WHIFF_1))#If player 1 punches and player 2 is not adjacent then nothing happens
    E.add_constraint((P_2&~adjacent)>>(WHIFF_2))
    #Compiling and returning theory
    return E

if __name__ == "__main__":

    T = game()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    #print("\nVariable likelihoods:")
    #for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        #print(" %s: %.2f" % (vn, likelihood(T, v)))
    #print()

