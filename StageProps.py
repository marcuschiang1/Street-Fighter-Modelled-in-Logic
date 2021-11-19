from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
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

def playerPositions():
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