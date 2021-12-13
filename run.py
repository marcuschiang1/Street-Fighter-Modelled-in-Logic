
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
class p1Counter:
    def __init__(self, data):
        self.data = data
        self.type = "p1Counter"
    def __repr__(self):
        return f"p1.{self.data}"
C_1 = p1Counter("COUNTER")

lightP_1 = p1Attack("Light Punch",2,3,"mid") #Player 1 performs a punch (adjacent)
overheadP_1 = p1Attack("Overhead punch",2,22,"overhead")
crouchKick_1 = p1Attack("Crouching Kick",3,6,"low")
standK_1 = p1Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_1 = p1Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_1 = p1Attack("Hadouken",7,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_1 = p1Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_1 = p1Action("HighBlock") #PLayer1 is blocking high
LB_1 = p1Action("LowBlock") #Player1 is blocking Low
NJUMP_1 = p1Action("Neutral Jump") #Player 1 jumps (mostly defensive)
FJUMP_1 = p1Action("Forward Jump") #Player 1 jumps (mostly offensive)
MB_1 = (LB_1|HB_1)

#
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
C_2 = p2Counter("COUNTER")
#Propositions for player 2 
lightP_2 = p2Attack("Light Punch",2,3,"mid" ) #Player 1 performs a punch (adjacent)
overheadP_2 = p2Attack("Overhead punch",2,22,"overhead")
crouchKick_2 = p2Attack("Crouching Kick",3,6,"low")
standK_2 = p2Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_2 = p2Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_2 = p2Attack("Hadouken",7,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_2 = p2Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_2 = p2Action("HighBlock") #Player 2 is blocking high
LB_2 = p2Action("LowBlock") #Player 2 is blocking Low
NJUMP_2 = p2Action("Neutral Jump") #Player 2 jumps (mostly defensive)
FJUMP_2 = p2Action("Forward Jump") #Player 2 jumps (mostly offensive)
MB_2 = (LB_2|HB_2)

#Both

############################################# Stage
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


#Propositions pertaining to both players


def rangeConstraint(action,p1position,p2position):
    if (abs(p1position.position-p2position.position)>action.range):
        E.add_constraint(~(p1position&p2position&action))
def counterHitCheck(p1position,p1attack,p2position,p2attack):
    if(abs(p1position.position-p2position.position)<p2attack.range):
        if(p1attack.startUp<p2attack.startUp):
            return True



        


#############################################
p1AttackArray = [lightP_1,overheadP_1,standK_1,crouchKick_1,T_1,H_1,SHORYU_1]
p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1]
p2AttackArray = [lightP_2,overheadP_2,standK_2,crouchKick_2,T_2,H_2,SHORYU_2]
p2ActionArray = [HB_2,LB_2,FJUMP_2,NJUMP_1]
eitherJump1 = (FJUMP_1|NJUMP_1)
eitherJump2 = (FJUMP_2|NJUMP_2)
def flawlessDefence():
    for attack in p1AttackArray:
        E.add_constraint(~attack)
    E.add_constraint(~FJUMP_1)
    E.add_constraint(~NJUMP_1)
    for p1position,p2position in zip(p1PositionArray,p2PositionArray):#Both players may not be in the same position
        E.add_constraint(~(p1position&p2position))
    E.add_constraint(~HB_2)
    E.add_constraint(~LB_2)
    for subset in combination(p1ActionArray,2):#Cannot perform any 2 actions at once
        E.add_constraint(~(subset[0]&subset[1]))
    for subset in combination(p1AttackArray,2):#Cannot perform any 2 attacks at once
        E.add_constraint(~(subset[0]&subset[1]))
    for i in range(len(p1AttackArray)-1):#Cannot perform and attack and block at the same time
        E.add_constraint(~(p1AttackArray[i]& MB_1))
    for i in range(1,len(p1ActionArray)-1):#Cannot perform either jump and block at the same time
        E.add_constraint(~(MB_1&p1AttackArray[i]))
    for i in range(2,len(p1AttackArray)-1):#Cannot perform attacks that are not punch or kick and jump at the same time
        E.add_constraint(~(NJUMP_1&p1AttackArray[i]))
        E.add_constraint(~(FJUMP_1&p1AttackArray[i]))
    #Player 2 limitations
    for subset in combination(p2ActionArray,2):#Cannot perform any 2 actions at once
        E.add_constraint(~(subset[0]&subset[1]))
    for subset in combination(p2AttackArray,2):#Cannot perform any 2 attacks at once
        E.add_constraint(~(subset[0]&subset[1]))
    for i in range(len(p2AttackArray)-1):#Cannot perform and attack and block at the same time
        E.add_constraint(~(p2AttackArray[i]&MB_1))
    for i in range(1,len(p2ActionArray)-1):#Cannot perform either jump and block at the same time
        E.add_constraint(~(MB_1&p2AttackArray[i]))
    for i in range(2,len(p2AttackArray)-1):
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
    #Rules:
    #High/Low
    for attack in p2AttackArray:
        if (attack.blockType == "overhead"):
            E.add_constraint(~(attack&~(HB_1)))
        if (attack.blockType == "mid"):
            E.add_constraint(~(attack&~(MB_1)))
        if (attack.blockType == "low"):
            E.add_constraint(~(attack&~(LB_1)))
        if (attack.blockType == "unblockable"):
            E.add_constraint(~attack&~(T_1|eitherJump1))
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
    print("\nLikelihood for player 1 to perform a certain action:")
    p1AttackArray = [lightP_1,overheadP_1,standK_1,crouchKick_1,T_1,H_1,SHORYU_1]
    p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1]
    p1CombinedArray = p1AttackArray+p1ActionArray
    head = ["Player1 attack",  "Player1 position","Player2 attack", "Player2 position"]
    variable = []*4
  
    for key,value in D.solve().items():
        if value == True:
            if (key.type == "p1Attack"):
                variable.append(key)
            elif (key.type == "p1Action"):
                variable.append(key)
            elif (key.type == "p1Position"):
                variable.append(key)
            elif (key.type == "p2Attack"):
                variable.append(key)
            elif (key.type == "p2Action"):
                variable.append(key)
            elif (key.type == "p2Position"):
                variable.append(key)
    alist = [0]*6
    for key,element in zip(variable,alist):
        element = key.data
    for v,vn in zip(p1CombinedArray, 'pPkKTHSBbFN'):
        print(" %s: %.2f" % (vn, likelihood(D, v)))
    print(len(D.vars()))
    print(len(D))
    print(tabulate(variable, alist, tablefmt="fancy_grid"))
    

    
    
