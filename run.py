
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
############################################# Players
@proposition(E)
class p1Attack:
    def __init__(self,data, range):
        self.data = data
        self.range = range
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1Action:
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return f"p1.{self.data}"
P_1 = p1Attack("Punch",1) #Player 1 performs a punch (adjacent)
K_1 = p1Attack("Kick",2) #Player 1 performs a kick (one space between)
T_1 = p1Attack("Throw",0) #Player 1 performs a throw (adjacent)
H_1 = p1Attack("Hadouken",3) #Player 1 has performed a H (2 spaces between)
SHORYU_1 = p1Attack("Shoryuken",0) #Player 1 has performed a shoryuken (Beats MP)
B_1 = p1Action("Block") #Player 1 is blocking 
NJUMP_1 = p1Action("Neutral Jump") #Player 1 jumps (mostly defensive)
FJUMP_1 = p1Action("Forward Jump") #Player 1 jumps (mostly offensive)
#
@constraint.exactly_one(E)
@proposition(E)
class p2Attack:
    def __init__(self,data, range):
        self.data = data
        self.range = range
    def __repr__(self):
        return f"p2.{self.data}"
@proposition(E)
class p2Action:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"p2position.{self.data}"

#Propositions for player 2 
P_2 = p2Attack("Punch",1) #Player 2 performs a punch
K_2 = p2Attack("Kick",2) #Player 2 performs a kick
T_2 = p2Attack("Throw",0) #Player 2 performs a throw
H_2 = p2Attack("Hadouken",3) #Player 2 has performed a H
SHORYU_2 = p2Attack("Shoryuken",0) #Player 2 has performed a shoryuken
B_2 = p2Action("Block") #Player 2 is blocking
NJUMP_2 = p2Action("Neutral Jump") #Player 2 jumps (mostly defensive)
FJUMP_2 = p2Action("Forward Jump") #Player 2 jumps (mostly offensive)

#Both

############################################# Stage
@constraint.exactly_one(E)
@proposition(E)
class p1Position:
    def __init__(self, position):
        self.position = position
    def __repr__(self):
        return f"p1Position.{self.position}"

@constraint.exactly_one(E)
@proposition(E)
class p2Position:
    def __init__(self, position):
        self.position = position
    def __repr__(self):
        return f"p2Position.{self.position}"

p1PositionArray = [p1Position(1),p1Position(2),p1Position(3),p1Position(4),p1Position(5),p1Position(6)]
p2PositionArray = [p2Position(1),p2Position(2),p2Position(3),p2Position(4),p2Position(5),p2Position(6)]
for i in range(len(p1PositionArray)-1):#Both players may not be in the same position
    E.add_constraint(~(p1PositionArray[i]&p2PositionArray[i]))
#Propositions pertaining to both players
p1AttackArray = [P_1,K_1,T_1,H_1,SHORYU_1]
p1ActionArray = [B_1,FJUMP_1,NJUMP_1]
p2AttackArray = [P_2,K_2,T_2,H_2,SHORYU_2]
p2ActionArray = [B_2,FJUMP_2,NJUMP_2]
eitherJump1 = (FJUMP_1|NJUMP_1)
eitherJump2 = (FJUMP_2|NJUMP_2)
def rangeConstraint(action,p1position,p2position):
    if (abs(p1position.position-p2position.position)>action.range):
        E.add_constraint(~(p1position&p2position&action))
    
#############################################

def flawlessDefence():
    E.add_constraint(~B_2)
    #Player 1 limitations
    for subset in combination(p1ActionArray,2):#Cannot perform any 2 actions at once
        E.add_constraint(~(subset[0]&subset[1]))
    for subset in combination(p1AttackArray,2):#Cannot perform any 2 attacks at once
        E.add_constraint(~(subset[0]&subset[1]))
    for i in range(len(p1AttackArray)-1):#Cannot perform and attack and block at the same time
        E.add_constraint(~(p1AttackArray[i]&B_1))
    for i in range(1,len(p1ActionArray)-1):#Cannot perform either jump and block at the same time
        E.add_constraint(~(B_1&p1AttackArray[i]))
    #P1 Range
    for p1position in p1PositionArray:
        for p2position in p2PositionArray:
            for attack in p1AttackArray:
                rangeConstraint(attack,p1position,p2position)
    #P2 Range
    for p2position in p2PositionArray:
        for p1position in p1PositionArray:
            for attack in p2AttackArray:
                rangeConstraint(attack,p2position,p1position)

    #From here on, range is covered. Do not need to include range in constraints since they already may not happen when not in range.
    #Punches
    E.add_constraint(~(P_2&~(B_1|eitherJump1|SHORYU_1)))#Player one must block, jump, or dp a punch
    E.add_constraint(~(P_2&K_1))
    #Kicks
    E.add_constraint(~(K_2&~(B_1|eitherJump1|SHORYU_1|(P_1))))#Player one may block, jump, or dp a kick.
    #Throws 
    E.add_constraint(~(T_2&~(T_1|P_1)))#Player 1 must throw back if thrown
    E.add_constraint(~(T_2&SHORYU_1))#Player 1 may not dp a throw
    #Fireballs
    E.add_constraint(~(H_2&~(eitherJump1|B_1|(H_1)|SHORYU_1|K_1|P_1)))#Player 1 just jump, block, fire their own hadouken, or stuff theirs
    #Shoryukens
    E.add_constraint(~(SHORYU_2&~(T_1|B_1)))
    
    #Compiling and returning theory
    return E

if __name__ == "__main__":

    D = flawlessDefence()
    
    # Don't compile until you're finished adding all your constraints!
    D = D.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    pprint.pprint("\nSatisfiable: %s" % D.satisfiable())
    print("# Solutions: %d" % count_solutions(D))
    pprint.pprint("Solution:")
    pprint.pprint(D.solve())
    #print("\nLikelihood for player 1 to perform a certain action:")
    p1ActionArray = [P_1,K_1,H_1,SHORYU_1,T_1,NJUMP_1,FJUMP_1,B_1]
    #p2ActionArray = [P_2,K_2,H_1,SHORYU_1,T_1,NJUMP_2,FJUMP_2,B_2]
    #for v,vn in zip(p1ActionArray, 'PKHSTNFB'):
        #print(" %s: %.2f" % (vn, likelihood(D, v)))
    print(len(D.vars()))
    print(len(D))
    
    