from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from StageProps import*
from PlayerProps import*

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BProp:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"
def constraints():
    E.add_constraint(~(P_1&K_1))
    E.add_constraint(~(P_2&K_2))#Player 1 nor 2 may perform a kick and punch at the same time
    E.add_constraint(H_1&JUMP_2)#Player 2 may jump to not get hit by a player 1 H
    E.add_constraint(H_2&JUMP_1)#The converse is also true
    E.add_constraint(((T_1&T_2)&(adjacent))>>bothNeutral)#Throw break
    E.add_constraint(((B_1)&(T_2))&adjacent)#Throwing a blocking opponent works
    E.add_constraint((P_1&~adjacent)>>(WHIFF_1))#If player 1 punches and player 2 is not adjacent then nothing happens
    E.add_constraint((P_2&~adjacent)>>(WHIFF_2))
    E.add_constraint(((P_1|K_1|H_1|SHORYU_1)&B_2)>>bothNeutral)#If player 2 is blocking and player 1 does an attack then nothing happens
    E.add_constraint(((P_2|K_2|H_2|SHORYU_1)&B_1)>>bothNeutral)
    E.add_constraint(((twoSpacesBetween|threeSpacesBetween|fourSpacesBetween)&K_1)>>WHIFF_1)#If player 1 or 2 uses kick and they are within 2,3,4 spaces then kick does nothing
    E.add_constraint((H_1)&(fourSpacesBetween)>>WHIFF_1)#Attack H does not work when player is there is four spaces between players
    E.add_constraint((H_2&fourSpacesBetween)>>WHIFF_2)