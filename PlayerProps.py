from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from StageProps import*
from RulesConstraints import*

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@constraint.add_exactly_one(E)
@proposition(E)
class p1Action:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
@proposition(E)
class p1State:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
def p1Propositions():
    W_1 = p1Action("W_1") #Player 1 wins
    D_1 = p1Action("D_1") #Player 1 has been damaged
    P_1 = p1Action("P_1") #Player 1 performs a punch (range of 1 space)
    K_1 = p1Action("K_1") #Player 1 performs a kick (range of 2 spaces)
    T_1 = p1Action("T_1") #Player 1 performs a throw
    B_1 = p1Action("B_1") #Player 1 is blocking
    JUMP_1 = p1Action("JUMP_1") #Player 1 jumps
    H_1 = p1Action("H_1") #Player 1 has performed a H (range of 3 spaces)
    SHORYU_1 = p1Action("SHORYU_1") #Player 1 has performed a shoryuken (Beats MP)
    NEUTRAL_1 = p1State("NEUTRAL_1")#Player 1 is in a neutral positions
    WHIFF_1 = p1State("WHIFF_1") #Player 1 whiffed their attack

@constraint.add_exactly_one(E)
@proposition(E)
class p2Action:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
@proposition(E)
class p2State:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
#Propositions for player 2 (The NPC)
def p2Propositions():
    W_2 = p2Action("W_2") #Player 2 wins
    D_2 = p2Action("D_2") #Player 2 has been damaged
    P_2 = p2Action("P_2") #Player 2 performs a punch
    K_2 = p2Action("K_2") #Player 2 performs a kick
    T_2 = p2Action("T_2") #Player 2 performs a throw
    B_2 = p2Action("B_2") #Player 2 is blocking
    JUMP_2 = p2Action("JUMP_2") #Player 2 jumps
    H_2 = p2Action("H_2") #Player 2 has performed a H
    SHORYU_2 = p2Action("SHORYU_2") #Player 2 has performed a shoryuken
    NEUTRAL_2 = p2State("NEUTRAL_2")#Player 2 is in a neutral positions
    WHIFF_2 = p2State("WHIFF_2") #Player 2 whiffed their attack

#Both
def bothPlayerProposition():
    bothNeutral = (NEUTRAL_1&NEUTRAL_2)