
from bauhaus import Encoding, proposition, constraint
from bauhaus.core import print_theory
from bauhaus.utils import count_solutions, likelihood
from tabulate import tabulate
import pprint
import itertools


# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
# Encoding that will store all of your constraints
E = Encoding()
#Player 1
@proposition(E)
class p1Attack:
    def __init__(self,data, range, startUp, blockType):
        self.data = data
        self.range = range
        self.startUp = startUp #Startup speed (lower is better cause less startup frames, 60fps game), a 3 frame move is 3/60 seconds   
        self.blockType = blockType #Overhead or low
        self.type = "p1Attack"
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1Action:
    def __init__(self, data):
        self.data = data
        self.type = "p1Action"
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1Interaction:
    def __init__(self, data):
        self.data = data
        self.type = "p1Counter"
    def __repr__(self):
        return f"p1.{self.data}"
C_1 = p1Interaction("COUNTER")
Trade_1 = p1Interaction("TRADE")
throwBreak_1 = p1Interaction("THROW BREAK")
lightP_1 = p1Attack("Light Punch",1,3,"mid") #Player 1 performs a punch (adjacent)
overheadP_1 = p1Attack("Overhead punch",2,22,"overhead")
crouchK_1 = p1Attack("Crouching Kick",3,6,"low")
standK_1 = p1Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_1 = p1Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_1 = p1Attack("Hadouken",7,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_1 = p1Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_1 = p1Action("HighBlock") #PLayer1 is blocking high
LB_1 = p1Action("LowBlock") #Player1 is blocking Low
NJUMP_1 = p1Action("Neutral Jump") #Player 1 jumps
FJUMP_1 = p1Action("Forward Jump") #Player 1 jumps
MB_1 = (LB_1|HB_1)

#Player 2
@constraint.exactly_one(E)
@proposition(E)
class p2Attack:
    def __init__(self,data, range,startUp,blockType):
        self.data = data
        self.range = range
        self.startUp = startUp
        self.blockType = blockType
        self.type = "p2Attack"
    def __repr__(self):
        return f"p2.{self.data}"
@proposition(E)
class p2Action:
    def __init__(self, data):
        self.data = data
        self.type = "p2Action"
    def __repr__(self):
        return f"p2.{self.data}"
@proposition(E)
class p2Counter:
    def __init__(self, data):
        self.data = data
        self.type = "p2Counter"
    def __repr__(self):
        return f"p2.{self.data}"
#Propositions for player 2 
lightP_2 = p2Attack("Light Punch",2,3,"mid" ) #Player 1 performs a punch (adjacent)
overheadP_2 = p2Attack("Overhead punch",2,22,"overhead")
crouchK_2 = p2Attack("Crouching Kick",3,6,"low")
standK_2 = p2Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_2 = p2Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_2 = p2Attack("Hadouken",7,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_2 = p2Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_2 = p2Action("HighBlock") #Player 2 is blocking high
LB_2 = p2Action("LowBlock") #Player 2 is blocking Low
NJUMP_2 = p2Action("Neutral Jump") #Player 2 jumps (mostly defensive)
FJUMP_2 = p2Action("Forward Jump") #Player 2 jumps (mostly offensive)
MB_2 = (LB_2|HB_2)

#Player Positions
@constraint.exactly_one(E)
@proposition(E)
class p1Position:
    def __init__(self, position):
        self.position = position
        self.type = "p1Position"
        self.data = position
    def __repr__(self):
        return f"p1Position.{self.position}"
@constraint.exactly_one(E)
@proposition(E)
class p2Position:
    def __init__(self, position):
        self.position = position
        self.type = "p2Position"
        self.data = position
    def __repr__(self):
        return f"p2Position.{self.position}"
p1PositionArray = [p1Position(1),p1Position(2),p1Position(3),p1Position(4),p1Position(5),p1Position(6),p1Position(7),p1Position(8),p1Position(9),p1Position(10)]
p2PositionArray = [p2Position(1),p2Position(2),p2Position(3),p2Position(4),p2Position(5),p2Position(6),p2Position(7),p2Position(8),p2Position(9),p2Position(10)]
#Functions
def counterHitConstraint(p1counterhit,p1position,p1attack,p2position,p2attack):
    if ((p1attack.startUp>=p2attack.startUp)):
        E.add_constraint(~(p1counterhit&(p1position&p1attack&p2position&p2attack)))
def rangeConstraint(action,p1position,p2position):
    if (abs(p1position.position-p2position.position)>action.range):
        E.add_constraint(~(p1position&p2position&action))
def combination(arr,r):
    return list(itertools.combinations(arr,r))
def trade(tradeVar,p1attack,p2attack):
    if ((p1attack.startUp!=p2attack.startUp)):
        E.add_constraint(~(tradeVar&(p1attack&p2attack)))
def throwBreak(breakVar,p1attack,p2attack):
    if ((p1attack.blockType != "unblockable" and p2attack.blockType != "unblockable")):
        E.add_constraint(~(breakVar&p1attack&p2attack))
#THEORIES
p1AttackArray = [lightP_1,standK_1,overheadP_1,crouchK_1,T_1,H_1,SHORYU_1]
p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1]
p2AttackArray = [lightP_2,standK_2,overheadP_2,crouchK_2,T_2,H_2,SHORYU_2]
p2ActionArray = [HB_2,LB_2,FJUMP_2,NJUMP_1]
eitherJump1 = (FJUMP_1|NJUMP_1)
eitherJump2 = (FJUMP_2|NJUMP_2)

def defence():
    E.add_constraint(~MB_2)
    E.add_constraint(lightP_1|overheadP_1|standK_1|crouchK_1|T_1|H_1|SHORYU_1|HB_1|LB_1|FJUMP_1|NJUMP_1)#Player 1 has to do something, they cannot just sit there
    for p1position,p2position in zip(p1PositionArray,p2PositionArray):#Both players may not be in the same position
        E.add_constraint(~(p1position&p2position))
    for subset in combination(p1ActionArray,2):#Cannot perform any 2 actions at once
        E.add_constraint(~(subset[0]&subset[1]))
    for subset in combination(p1AttackArray,2):#Cannot perform any 2 attacks at once
        E.add_constraint(~(subset[0]&subset[1]))
    for i in range(len(p1AttackArray)-1):#Cannot perform an attack and block at the same time
        E.add_constraint(~(p1AttackArray[i]& MB_1))
    #Cannot perform either jump and block
    E.add_constraint(~(eitherJump1&MB_1))
    #Cannot perform attacks and jump
    for i in range(len(p1AttackArray)-1):
        E.add_constraint(~(eitherJump1&p1AttackArray[i]))
    #Player 2 limitations
    for subset in combination(p2ActionArray,2):#Cannot perform any 2 actions at once
        E.add_constraint(~(subset[0]&subset[1]))
    for subset in combination(p2AttackArray,2):#Cannot perform any 2 attacks at once
        E.add_constraint(~(subset[0]&subset[1]))
    for i in range(len(p2AttackArray)-1):#Cannot perform and attack and block at the same time
        E.add_constraint(~(p2AttackArray[i]&MB_2))
    for i in range(1,len(p2ActionArray)-1):#Cannot perform either jump and block at the same time
        E.add_constraint(~(MB_2&p2AttackArray[i]))
    for i in range(2,len(p2AttackArray)-1):#Cannot do either jump and certain attacks
        E.add_constraint(~(NJUMP_2&p2AttackArray[i]))
        E.add_constraint(~(FJUMP_2&p2AttackArray[i]))
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
    #Counterhit (this makes it so C_1 is not true if p1 does not perform a counter hit)
    for p1position in p1PositionArray:
        for p2position in p2PositionArray:
            for p1attack in p1AttackArray:
                for p2attack in p2AttackArray:
                    counterHitConstraint(C_1,p1attack,p2attack)
                    trade(Trade_1,p1position,p1attack,p2position,p2attack)
                    throwBreak(throwBreak_1,p1attack,p2attack)
    for p1action in p1ActionArray:
        E.add_constraint(~(C_1&p1action))
    for p1action in p1ActionArray:
        E.add_constraint(~(Trade_1&p1action))
    #StartUp (this is to make sure that player1 will not perform an attack that is slower than player2 attack, range already accounted for above)
    #Have to bind each attack constraint to a range, or else the attacks will be completely negated for all positions
    for p1attack in p1AttackArray:
        for p2attack in p2AttackArray:
            if (p1attack.startUp>p2attack.startUp):
                E.add_constraint(~(p1attack&p2attack))
    #Rules:
    #High/Low blocking
    for attack in p2AttackArray:
        if (attack.blockType == "overhead"):
            E.add_constraint(~(attack&LB_1))
        if (attack.blockType == "low"):
            E.add_constraint(~(attack&HB_1))
    
    return E

if __name__ == "__main__":
    D = defence()
    # Don't compile until you're finished adding all your constraints!
    D = D.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    pprint.pprint("\nSatisfiable: %s" % D.satisfiable())
    print("# Solutions: %d" % count_solutions(D))
    pprint.pprint("Solution:")
    pprint.pprint(D.solve())
    print("\nLikelihood for player 1 to perform a certain action:")
    p1AttackArray = [lightP_1,overheadP_1,standK_1,crouchK_1,T_1,H_1,SHORYU_1]
    p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1,C_1,Trade_1,throwBreak_1]
    p1CombinedArray = p1AttackArray+p1ActionArray
    
    for v,vn in zip(p1CombinedArray, 'pPkKTHSBbFNCtQ'):
        print(" %s: %.2f" % (vn, likelihood(D, v)))
    
    print("\nLikelihood for player 2 to perform a certain action:")
    p2AttackArray = [lightP_2,overheadP_2,standK_2,crouchK_2,T_2,H_2,SHORYU_2]
    p2ActionArray = [HB_2,LB_2,FJUMP_2,NJUMP_2]
    p2CombinedArray = p2AttackArray+p2ActionArray
    
    for v,vn in zip(p2CombinedArray, 'pPkKTHSBbFNt'):
        print(" %s: %.2f" % (vn, likelihood(D, v)))
    print(len(D.vars()))
    print(len(D))
  
    

    
    
