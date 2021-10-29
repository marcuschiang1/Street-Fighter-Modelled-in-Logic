
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BProp:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for propositions are useful because this allows for more dynamic constraint creation
# for propositions within that class. For example, you can enforce that "at least one" of the propositions
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositions:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

# Call your variables whatever you want
#Propositions for player 1 
W_1 = BProp("W_1") #Player 1 wins
D_1 = BProp("D_1") #Player 1 has been damaged
P_1 = BProp("P_1") #Player 1 performs a punch (range of 1 space)
K_1 = BProp("K_1") #Player 1 performs a kick (range of 2 spaces)
T_1 = BProp("T_1") #Player 1 performs a throw
JUMP_1 = BProp("JUMP_1") #Player 1 jumps
HADOUKEN_1 = BProp("HADOUKEN_1") #Player 1 has performed a hadouken (range of 3 spaces)
SHORYU_1 = BProp("SHORYU_1") #Player 1 has performed a shoryuken (Beats MP)
NEUTRAL_1 = BProp("NEUTRAL_1")#Player 1 is in a neutral positions
P1position = [0]*6
for i in range(6):
    P1position[i] =  BProp("SPACE_1_"+str(i)) #SPACE_1_3 means that player 1 is in space 3, access p1 in space 3 by P1position[2]

#Player 1 inputs
I_P = BProp("I_P_1")
I_K = BProp("I_K_1")
directionalInputs = [0]*10 #Array for directional inputs with each index corresponding to it's number on a keypad
for i in range(10):
    directionalInputs[i] =  BProp("I_"+str(i))
print(directionalInputs) 
#Propositions for player 2 (The NPC)
W_2 = BProp("W_2") #Player 2 wins
D_2 = BProp("D_2") #Player 2 has been damaged
P_2 = BProp("P_2") #Player 2 performs a punch
K_2 = BProp("K_2") #Player 2 performs a kick
T_2 = BProp("T_2") #Player 2 performs a throw
JUMP_2 = BProp("JUMP_2") #Player 2 jumps
HADOUKEN_2 = BProp("HADOUKEN_2") #Player 2 has performed a hadouken
SHORYU_2 = BProp("SHORYU_2") #Player 2 has performed a shoryuken
NEUTRAL_2 = BProp("NEUTRAL_2")#Player 2 is in a neutral positions
P2position = [0]*6 #Same as p1 positions, but for p2
for i in range(6):
    P2position[i] =  BProp("SPACE_2_"+str(i))

#Propositions pertaining to both players
fourSpacesBetween = ((P1position[0]&P2position[5])|(P1position[5]&P2position[0]))#In the first and last spots, also converse
threeSpacesBetween = ((P1position[0]&P2position[4])|(P1position[4]&P2position[0])|(P1position[1]&P2position[5])|(P1position[5]&P2position[1]))
twoSpacesBetween = ((P1position[0]&P2position[3])|(P1position[3]&P2position[0])|(P1position[1]&P2position[4])|(P1position[4]&P2position[1])|(P1position[2]&P2position[5])|(P1position[5]&P2position[2]))
oneSpaceBetweem = ((P1position[0]&P2position[2])|(P1position[2]&P2position[0])|(P1position[1]&P2position[3])|(P1position[3]&P2position[1])|(P1position[2]&P2position[4])|(P1position[4]&P2position[2])|(P1position[3]&P2position[5])|(P1position[5]&P2position[3]))
#Adjacent would be 0 spaces away, right next to eachother
adjacent = ((P1position[0]&P2position[1])|(P1position[1]&P2position[2])|(P1position[2]&P2position[3])|(P1position[3]&P2position[4])|(P1position[4]&P2position[5])|(P1position[1]&P2position[0])|(P1position[2]&P2position[1])|(P1position[3]&P2position[2])|(P1position[4]&P2position[3])|(P1position[5]&P2position[4]))
bothNeutral = (NEUTRAL_1&NEUTRAL_2)
#Player 2 has no inputs since they are NPC, so no input propositions

# At least one of these will be true
x = FancyPropositions("x")
y = FancyPropositions("y")
z = FancyPropositions("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    #E.add_constraint((a | b) & ~x)
    # Implication
    #E.add_constraint(y >> z)
    # Negate a formula
    #E.add_constraint((x & y).negate())
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BProp, but you want to enforce it for a, b, and c.:
    #constraint.add_exactly_one(E, a, b, c)
    #Our constraints
    E.add_constraint((I_P & I_K)>>T_1) #Punch and kick from a player results in a throw
    #E.add_constraint((P_1&K_1).negate())
    #E.add_constraint((P_2&K_2).negate())#Player 1 nor 2 may perform a kick and punch at the same time
    E.add_constraint(HADOUKEN_1&JUMP_2)#Player 2 may jump to not get hit by a player 1 hadouken
    E.add_constraint(HADOUKEN_2&JUMP_1)#The converse is also true
    E.add_constraint(((T_1&T_2)&(adjacent))>>bothNeutral)


    return E


if __name__ == "__main__":

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()
    # After compilation (and only after), you can check some of the properties
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    for v,vn in zip([a,b,c,x,y,z], 'abcxyz'):
        # Ensure that you only send these functions NNF formulas
        # Literals are compiled to NNF here
        print(" %s: %.2f" % (vn, likelihood(T, v)))
    print()