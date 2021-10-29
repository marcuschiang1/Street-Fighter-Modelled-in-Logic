
from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Encoding that will store all of your constraints
E = Encoding()

# To create propositions, create classes for them first, annotated with "@proposition" and the Encoding
@proposition(E)
class BasicPropositions:

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


d = {}

for i in range(1,10):

    d["I_{0}".format(i)] = BasicPropositions()
    
    
W_1 = BasicPropositions("W_1") #Player 1 wins
D_1 = BasicPropositions("D_1") #Player 1 has been damaged
LP_1 = BasicPropositions("LP_1") #Player 1 performs a light punch
MP_1 = BasicPropositions("MP_1") #Player 1 performs a medium punch
HP_1 = BasicPropositions("HP_1") #Player 1 performs a heavy punch
LK_1 = BasicPropositions("LK_1") #Player 1 performs a light kick
MK_1 = BasicPropositions("MK_1") #Player 1 performs a medium kick
HK_1 = BasicPropositions("HK_1") #Player 1 performs a heavy kick
T_1 = BasicPropositions("T_1") #Player 1 performs a throw
HADOUKEN_1 = BasicPropositions("HADOUKEN_1") #Player 1 has performed a hadouken
SHORYU_1 = BasicPropositions("SHORYU_1") #Player 1 has performed a shoryuken
SPACE1_1 = BasicPropositions("SPACE1_1") #Player 1 in space 1
SPACE2_1 = BasicPropositions("SPACE2_1") #Player 1 in space 2
SPACE3_1 = BasicPropositions("SPACE3_1") #Player 1 in space 3
WHIFF_1 = BasicPropositions("WHIFF_1") #Player 1 whiffed their attack
#Player 1 inputs
I_LP = BasicPropositions("I_LP") #Light punch input
I_MP = BasicPropositions("I_MP") #Medium punch input
I_HP = BasicPropositions("I_HP") #Heavy punch input
I_LK = BasicPropositions("I_LK") #Light kick input
I_MK = BasicPropositions("I_MK") #Medium kick input 
I_HK = BasicPropositions("I_HK") #Heavy kick input


#using dictionary for variables
#using for loop to create dictionary


for i in range(1,10):

    d["I_{0}".format(i)] = BasicPropositions(Str(i))
    
    




I_1 = BasicPropositions("1") #Down back
I_2 = BasicPropositions("2") #Down
I_3 = BasicPropositions("3") #Down forward
I_4 = BasicPropositions("4") #Back
I_6 = BasicPropositions("6") #Forward
I_7 = BasicPropositions("7") #Up back
I_8 = BasicPropositions("8") #Up
I_9 = BasicPropositions("9") #Up forward

#Propostions for player 2 (The NPC)
W_2 = BasicPropositions("W_2") #Player 2 wins
D_2 = BasicPropositions("D_2") #Player 2 has been damaged
LP_2 = BasicPropositions("LP_2") #Player 2 performs a light punch
MP_2 = BasicPropositions("MP_2") #Player 2 performs a medium punch
HP_2 = BasicPropositions("HP_2") #Player 2 performs a heavy punch
LK_2 = BasicPropositions("LK_2") #Player 2 performs a light kick
MK_2 = BasicPropositions("MK_2") #Player 2 performs a medium kick
HK_2 = BasicPropositions("HK_2") #Player 2 performs a heavy kick
T_2 = BasicPropositions("T_2") #Player 2 performs a throw
HADOUKEN_2 = BasicPropositions("HADOUKEN_2") #Player 2 has performed a hadouken
SHORYU_2 = BasicPropositions("SHORYU_2") #Player 2 has performed a shoryuken
SPACE1_2 = BasicPropositions("SPACE1_2") #Player 2 in space 1
SPACE2_2 = BasicPropositions("SPACE2_2") #Player 2 in space 2
SPACE3_2 = BasicPropositions("SPACE3_2") #Player 2 in space 3
WHIFF_2 = BasicPropositions("WHIFF_2") #Player 2 whiffed their attack

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
    #Throw input
    E.add_constraint((I_LP_1 | I_LK_1)>>T_1)
    E.add_constraint((LP_1 & MP_1).negate())
    # Implication
    E.add_constraint((W_1 & W_2).negate()) #added constraints
    # Negate a formula
    E.add_constraint((D_1 & B_1).negate() | (D_2 & B_2).negate)
    
    
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositions, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

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
