from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from StageProps import*
from RulesConstraints import*

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BProp:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
def p1Propositions():
    W_1 = BProp("W_1") #Player 1 wins
    D_1 = BProp("D_1") #Player 1 has been damaged
    P_1 = BProp("P_1") #Player 1 performs a punch (range of 1 space)
    K_1 = BProp("K_1") #Player 1 performs a kick (range of 2 spaces)
    T_1 = BProp("T_1") #Player 1 performs a throw
    B_1 = BProp("B_1") #Player 1 is blocking
    JUMP_1 = BProp("JUMP_1") #Player 1 jumps
    H_1 = BProp("H_1") #Player 1 has performed a H (range of 3 spaces)
    SHORYU_1 = BProp("SHORYU_1") #Player 1 has performed a shoryuken (Beats MP)
    NEUTRAL_1 = BProp("NEUTRAL_1")#Player 1 is in a neutral positions
    WHIFF_1 = BProp("WHIFF_1") #Player 1 whiffed their attack

#Propositions for player 2 (The NPC)
def p2Propositions():
    W_2 = BProp("W_2") #Player 2 wins
    D_2 = BProp("D_2") #Player 2 has been damaged
    P_2 = BProp("P_2") #Player 2 performs a punch
    K_2 = BProp("K_2") #Player 2 performs a kick
    T_2 = BProp("T_2") #Player 2 performs a throw
    B_2 = BProp("B_2") #Player 2 is blocking
    JUMP_2 = BProp("JUMP_2") #Player 2 jumps
    H_2 = BProp("H_2") #Player 2 has performed a H
    SHORYU_2 = BProp("SHORYU_2") #Player 2 has performed a shoryuken
    NEUTRAL_2 = BProp("NEUTRAL_2")#Player 2 is in a neutral positions
    WHIFF_2 = BProp("WHIFF_2") #Player 2 whiffed their attack

#Both
def bothPlayerProposition():
    bothNeutral = (NEUTRAL_1&NEUTRAL_2)