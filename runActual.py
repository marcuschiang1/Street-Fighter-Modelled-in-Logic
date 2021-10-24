
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
W_1 = BasicPropositions("W_1") #Player 1 wins
D_1 = BasicPropositions("D_1") #Player 1 has been damaged
LP_1 = BasicPropositions("LP_1") #Player 1 performs a light punch
MP_1 = BasicPropositions("MP_1") #Player 1 performs a medium punch
HP_1 = BasicPropositions("HP_1") #Player 1 performs a heavy punch
LK_1 = BasicPropositions("LK_1") #Player 1 performs a light kick
MK_1 = BasicPropositions("MK_1") #Player 1 performs a medium kick
HK_1 = BasicPropositions("HK_1") #Player 1 performs a heavy kick
T_1 = BasicPropositions("T_1") #Player 1 performs a throw
#Player 1 inputs
I_LP = BasicPropositions("I_LP")
I_MP = BasicPropositions("I_MP")
I_HP = BasicPropositions("I_HP")
I_LK = BasicPropositions("I_LK")
I_MK = BasicPropositions("I_MK")
I_HK = BasicPropositions("I_HK")
#Propostions for player 2 (The NPC)
W_2 = BasicPropositions("W_2") #Player 2 wins
A_2 = BasicPropositions("A_2") #Player 2 performs an attack
D_2 = BasicPropositions("D_2") #Player 2 has been damaged

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
    E.add_constraint((LP_1 & MP_1).negate())
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint((x & y).negate())
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
