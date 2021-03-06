
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
class p1Attack: #Propositions for creating player 1 attacks
    def __init__(self,data, range, startUp, blockType):
        self.data = data #For representation
        self.range = range #How many spaces the move can move, relative to the position variables made later
        self.startUp = startUp #Startup speed (lower is better cause less startup frames, 60fps game), a 3 frame move is 3/60 seconds   
        self.blockType = blockType #Overhead or low
        self.type = "p1Attack" #Type for checking when printing table
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1Action: #player 1 actions, specifically actions they can take THAT ARE NOT ATTACKS
    def __init__(self, data):
        self.data = data #For representation
        self.type = "p1Action" #For sorting
    def __repr__(self):
        return f"p1.{self.data}"
@proposition(E)
class p1Interaction: #Indicates when a defensive move results in a counter hit or trade
    def __init__(self, data):
        self.data = data
        self.type = "p1Counter"
    def __repr__(self):
        return f"p1.{self.data}"
counter_1 = p1Interaction("COUNTER") #Is true when player 1 has landed a counter
trade_1 = p1Interaction("TRADE") #Is true when player 1 trades with the opponent
lightP_1 = p1Attack("Light Punch",1,3,"mid") #Player 1 performs a punch (adjacent)
overheadP_1 = p1Attack("Overhead punch",2,22,"overhead") #Player 1 performs an overhead attack with 2 range and 22 frames of startup
crouchK_1 = p1Attack("Crouching Kick",3,6,"low") #
standK_1 = p1Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_1 = p1Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_1 = p1Attack("Hadouken",8,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_1 = p1Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_1 = p1Action("HighBlock") #Player1 is blocking high
LB_1 = p1Action("LowBlock") #Player1 is blocking Low
NJUMP_1 = p1Action("Neutral Jump") #Player 1 jumps
FJUMP_1 = p1Action("Forward Jump") #Player 1 jumps
MB_1 = (LB_1|HB_1) #Mid
#Player 2
@constraint.exactly_one(E)
@proposition(E)
class p2Attack: #Same as player 1 attack, they are the same character
    def __init__(self,data, range,startUp,blockType):
        self.data = data
        self.range = range
        self.startUp = startUp
        self.blockType = blockType
        self.type = "p2Attack"
    def __repr__(self):
        return f"p2.{self.data}"
@proposition(E)
class p2Action: #Same as player 1
    def __init__(self, data):
        self.data = data
        self.type = "p2Action"
    def __repr__(self):
        return f"p2.{self.data}"
#Propositions for player 2 
lightP_2 = p2Attack("Light Punch",2,3,"mid" ) #Player 1 performs a punch (adjacent)
overheadP_2 = p2Attack("Overhead punch",2,22,"overhead")
crouchK_2 = p2Attack("Crouching Kick",3,6,"low")
standK_2 = p2Attack("Kick",4,8,"mid") #Player 1 performs a kick (one space between)
T_2 = p2Attack("Throw",1,5,"unblockable") #Player 1 performs a throw (adjacent)
H_2 = p2Attack("Hadouken",8,14,"mid") #Player 1 has performed a H (2 spaces between)
SHORYU_2 = p2Attack("Shoryuken",1,0,"mid") #Player 1 has performed a shoryuken (Beats MP)
HB_2 = p2Action("HighBlock") #Player 2 is blocking high
LB_2 = p2Action("LowBlock") #Player 2 is blocking Low
NJUMP_2 = p2Action("Neutral Jump") #Player 2 jumps (mostly defensive)
FJUMP_2 = p2Action("Forward Jump") #Player 2 jumps (mostly offensive)
MB_2 = (LB_2|HB_2)

#Player Positions
@constraint.exactly_one(E)
@proposition(E)
class p1Position: #Create position variables for player 1
    def __init__(self, position):
        self.position = position #Position is an integer
        self.type = "p1Position" #For sorting
        self.data = position #For sorting
    def __repr__(self):
        return f"p1Position.{self.position}"
@constraint.exactly_one(E)
@proposition(E)
class p2Position: #Same as player 1
    def __init__(self, position):
        self.position = position
        self.type = "p2Position"
        self.data = position
    def __repr__(self):
        return f"p2Position.{self.position}"
p1PositionArray = [p1Position(1),p1Position(2),p1Position(3),p1Position(4),p1Position(5),p1Position(6),p1Position(7),p1Position(8),p1Position(9),p1Position(10)]
p2PositionArray = [p2Position(1),p2Position(2),p2Position(3),p2Position(4),p2Position(5),p2Position(6),p2Position(7),p2Position(8),p2Position(9),p2Position(10)]
#Arrays containing all the possible positions that player 1 or player 2 could occupy
#Functions
def counterHit(counterVar,p1attack,p2attack): #If the attack of player 1 is faster than player 2, it will be a counter hit
    if (p1attack.startUp>p2attack.startUp): #Covering all situations in which a counter hit is not applicable (covering situations in which it is applicable creates problems)
        E.add_constraint(~(counterVar&p1attack&p2attack))
def trade(tradeVar,p1attack,p2attack): #If both players use the same move on eachother, it will trade
    if(p1attack.data != p2attack.data):
        E.add_constraint(~(tradeVar&p1attack&p2attack))
def rangeConstraint(action,p1position,p2position):#If the distance between two players is greater than the range of one of their moves, restrist that situation
    if (abs(p1position.position-p2position.position)>action.range):
        E.add_constraint(~(p1position&p2position&action))
def combination(arr,r):#Create combinations for constraints in theory
    return list(itertools.combinations(arr,r))

#THEORIES
p1AttackArray = [lightP_1,standK_1,overheadP_1,crouchK_1,T_1,H_1,SHORYU_1]
p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1]
p2AttackArray = [lightP_2,standK_2,overheadP_2,crouchK_2,T_2,H_2,SHORYU_2]
p2ActionArray = [HB_2,LB_2,FJUMP_2,NJUMP_1]
eitherJump1 = (FJUMP_1|NJUMP_1)
eitherJump2 = (FJUMP_2|NJUMP_2)

def defence():
    E.add_constraint(~HB_2) #Restrict player 2 from blocking, they are on offence
    E.add_constraint(~LB_2)
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
    for i in range(len(p2AttackArray)-1):#Cannot perform an attack and block at the same time
        E.add_constraint(~(p2AttackArray[i]& MB_2))
    #Cannot perform either jump and block
    E.add_constraint(~(eitherJump2&MB_2))
    #Cannot perform attacks and jump
    for i in range(len(p2AttackArray)-1):
        E.add_constraint(~(eitherJump2&p2AttackArray[i]))
    #P1 Range
    for p1position in p1PositionArray: #Uses the previously defined range function for all combinations for positions
        for p2position in p2PositionArray:
            for attack in p1AttackArray:
                rangeConstraint(attack,p1position,p2position)
    #P2 Range
    for p2position in p2PositionArray: #Same as p1 range, but for p2
        for p1position in p1PositionArray:
            for attack in p2AttackArray:
                rangeConstraint(attack,p2position,p1position)
    #Counterhit (this makes it so C_1 is not true if p1 does not perform a counter hit)
    for p1attack in p1AttackArray:
        for p2attack in p2AttackArray:
            counterHit(counter_1,p1attack,p2attack) #Checks each attacks range and speed to see if counter hit or trade
            trade(trade_1,p1attack,p2attack)
    for p1action in p1ActionArray: #Counterhit cannot occur when player 1 is not attacking
        E.add_constraint(~(counter_1&p1action))
    for p1action in p1ActionArray:
        E.add_constraint(~(trade_1&p1action))
    #Rules:
    #High/Low blocking
    for attack in p2AttackArray:
        if (attack.blockType == "overhead"):#If the attack type is overhead, player 1 cannot block low
            E.add_constraint(~(attack&LB_1))
        if (attack.blockType == "low"):
            E.add_constraint(~(attack&HB_1))#If the attack type is low, player 1 cannot block overhead
    #Fireballs
    E.add_constraint(~(H_2&~(eitherJump1|H_1|MB_1))) #Jump over, fireball back, or block
    #Shoryukens
    E.add_constraint(~(SHORYU_2&~(MB_1|T_1))) #Block or throw shoryukens
    return E
    

if __name__ == "__main__":
    for i in range(10):
        D = defence()
        D = D.compile()
        #pprint.pprint("\nSatisfiable: %s" % D.satisfiable())
        #print("# Solutions: %d" % count_solutions(D))
        #pprint.pprint("Solution:")
        #pprint.pprint(D.solve())
        #print("\nLikelihood for player 1 to perform a certain action:")
        p1AttackArray = [lightP_1,overheadP_1,standK_1,crouchK_1,T_1,H_1,SHORYU_1]
        p1ActionArray = [HB_1,LB_1,FJUMP_1,NJUMP_1,counter_1,trade_1]
        p1CombinedArray = p1AttackArray+p1ActionArray
        
    # Adding the outputs to a table, so that no matter what order the outputs come in, they will match up with the correct header.
        variable = [0]*6
        head = ["Player1 Action",  "Player1 position","Player2 position", "Player2 Attack","Counter","Trade"]

        for key,value in D.solve().items():
            if value == True:
                if (key.type == "p1Attack"):
                    variable[0] = (key.data)
                elif (key.type == "p1Counter"):
                    if key.data == "TRADE":
                        variable[4] = "False"
                        variable[5] = "True"
                    else:
                        variable[4] = "True"
                        variable[5] = "False"
                elif (key.type == "p1Position"):
                    variable[1] = (key.position)
                elif (key.type == "p2Attack"):
                    variable[3] = (key.data)
                elif (key.type == "p1Trade"):
                    if value == True:
                        variable[5] = "True"
                    else:
                        variable[5] = "False"
                elif (key.type == "p2Position"):
                    variable[2] = (key.position)
        
        wordArray = []
        for element in p1CombinedArray:
            wordArray.append(element.data)
        #for v,vn in zip(p1CombinedArray, wordArray):
            #print(" %s: %.2f" % (vn, likelihood(D, v)))
        mydata = []
        mydata.append(variable)
        print(tabulate(mydata, head, tablefmt="fancy_grid"))
    
    
