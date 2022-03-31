#
# <formel>::= <mol> \n
# <mol>   ::= <group> | <group><mol>
# <group> ::= <atom> |<atom><num> | (<mol>) <num>
# <atom>  ::= <LETTER> | <LETTER><letter>
# <LETTER>::= A | B | C | ... | Z
# <letter>::= a | b | c | ... | z
# <num>   ::= 2 | 3 | 4 | ...
#
# Pseudokod:
#
# Dela upp inmatade formler
# Titta på första gruppen i formeln
# Här kanske man kan göra snyggt som den där hemsidan, men med return f"{self.pos} ...."
class ParseError(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, formula):
        q_formula = Node(formula)
        if self.first is None:
            self.first = q_formula
            self.last = q_formula
        else:
            self.last.next = q_formula
            self.last = q_formula

    def dequeue(self):
        value = self.first.value
        self.first = self.first.next
        return value

    def peek(self):
        return self.first.value


# Grundämnen
atoms = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
         'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
         'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
         'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re',
         'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
         'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg',
         'Cn', 'Fl', 'Lv']


def readformulas(formulas):
    readmolecule()

    '''while True:
        molecule = formulas[0]
        readmolecule(molecule)
        if len(formulas) > 0:
            formulas.pop(0)
        else:
            break'''


# Formeln måste börja med "(" eller stor bokstav
def readmolecule(molecule):
    # Hämta ut
    readgroup(molecule)
    # Kolla om molekylen är färdig
    # Om molekylen inte är färdig, fortsätt med nästa grupp


def readgroup(molecule):
    if molecule[0].isupper():
        pass
    elif molecule[0] == "(":
        pass


def readatom():
    pass


def readletter():
    pass


def readnum():
    pass


def main():
    print("Mata in kemiska föreningar här:")

    formula_queue = Queue()

    while True:
        molecule = input("")
        if molecule == "#":
            break
        formula_queue.enqueue(molecule)
    readformulas(formula_queue)


# Startar programmet om programmet startar i denna fil. (Startar ej programmet ifall det kallas från en annan fil)
# (Behövs egentligen inte här)
if __name__ == "__main__":
    main()
