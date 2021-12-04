
from bauhaus import Encoding, proposition, constraint
from bauhaus.core import print_theory
from bauhaus.utils import count_solutions, likelihood
from tabulate import tabulate
import pprint
import itertools
def combination(arr,r):
    return list(itertools.combinations(arr,r))

# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
# Encoding that will store all of your constraints
E = Encoding()
C = Encoding()
############################################# Players
@proposition(E)

class p1Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1.{self.data}"
W_1 = p1Action("W") #Player 1 wins
P_1 = p1Action("P") #Player 1 performs a punch (adjacent)
K_1 = p1Action("K") #Player 1 performs a kick (one space between)
T_1 = p1Action("T") #Player 1 performs a throw (adjacent)
B_1 = p1Action("B") #Player 1 is blocking 
JUMP_1 = p1Action("JUMP") #Player 1 jumps (beats hadouken)
H_1 = p1Action("H") #Player 1 has performed a H (2 spaces between)
SHORYU_1 = p1Action("SHORYU") #Player 1 has performed a shoryuken (Beats MP)
p1ActionArray = [P_1,K_1,H_1,T_1,JUMP_1,B_1]
#
WHIFF_1 = p1State("WHIFF") #Player 1 whiffed their attack
D_1 = p1State("D") #Player 1 has been damaged
@constraint.exactly_one(E)
@proposition(E)
class p2Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p2.{self.data}"
@proposition(E)
class p2State:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p2.{self.data}"

#Propositions for player 2 
W_2 = p2Action("W") #Player 2 wins
P_2 = p2Action("P") #Player 2 performs a punch
K_2 = p2Action("K") #Player 2 performs a kick
T_2 = p2Action("T") #Player 2 performs a throw
B_2 = p2Action("B") #Player 2 is blocking
JUMP_2 = p2Action("JUMP") #Player 2 jumps
H_2 = p2Action("H") #Player 2 has performed a H
SHORYU_2 = p2Action("SHORYU") #Player 2 has performed a shoryuken
p2AttackArray = [P_2,K_2,T_2,H_2,SHORYU_2,B_1]
#
WHIFF_2 = p2State("WHIFF") #Player 2 whiffed their attack
D_2 = p2State("D") #Player 2 has been damaged
#Both

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

def defence():
    #Player 1 limitations
    for subset in combination(p1ActionArray,2):
        E.add_constraint(~(subset[0]&subset[1]))
    #P1 Range
    E.add_constraint(~(P_1&~adjacent))#Player 1 may not punch when not adjacent
    E.add_constraint(~(K_1&~(adjacent|oneSpaceBetween)))#Player 1 may not kick if not within one space
    E.add_constraint(~(H_1&~(adjacent|oneSpaceBetween|twoSpacesBetween)))#Player 1 may not hadouken if not within two spaces
    E.add_constraint(~(T_1&~adjacent))#Player 1 may not throw if not adjacent
    E.add_constraint(~(SHORYU_1&~adjacent))
    #P2 Range
    E.add_constraint(~(P_2&~adjacent))#Player 2 may not punch when not adjacent
    E.add_constraint(~(K_2&~(adjacent|oneSpaceBetween)))#Player 2 may not kick if not within one space
    E.add_constraint(~(H_2&~(adjacent|oneSpaceBetween|twoSpacesBetween)))#Player 2 may not hadouken if not within two spaces
    E.add_constraint(~(T_2&~adjacent))#Player 2 may not throw if not adjacent
    E.add_constraint(~(SHORYU_2&~adjacent))
    #From here on, range is covered. Do not need to include range in constraints since they already may not happen when not in range.
    #Punches
    E.add_constraint(~(P_2&~(B_1|JUMP_1|SHORYU_1)))#Player one must block, jump, or dp a punch
    E.add_constraint(~(P_2&K_2))
    #Kicks
    E.add_constraint(~(K_2&~(B_1|JUMP_1|SHORYU_1)))#Player one may block, jump, or dp a kick.
    #Throws 
    E.add_constraint(~(T_2&~(T_1|P_1)))#Player 1 must throw back if thrown
    E.add_constraint(~(T_2&SHORYU_1))#Player 1 may not dp a throw
    #Fireballs
    E.add_constraint(~(H_2&~(JUMP_1|B_1|H_1|SHORYU_1|K_1|P_1)))#Player 1 just jump, block, fire their own hadouken, or stuff theirs
    #Shoryukens
    E.add_constraint(~(SHORYU_2&~(T_1|B_1)))
    
    #Compiling and returning theory
    return E

if __name__ == "__main__":
    D = defence()
    # Don't compile until you're finished adding all your constraints!
    D = D.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    pprint.pprint("\nSatisfiable: %s" % D.satisfiable())
    print("# Solutions: %d" % count_solutions(D))
    pprint.pprint("   Solution: %s" % D.solve())

    print("\nLikelihood for player 1 to perform a certain action:")
    for v,vn in zip(p1ActionArray, 'PKTHSB'):
        print(" %s: %.2f" % (vn, likelihood(D, v)))
    