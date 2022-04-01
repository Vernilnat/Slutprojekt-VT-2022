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


# Enkel nod-objekt, värde och pekare på nästa
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        pass

    def enqueue(self, formula):
        q_formula = Node(formula)
        if self.first is None:
            self.first = q_formula
            self.last = q_formula
        else:
            self.last.next = q_formula
            self.last = q_formula

    def get(self):
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


def parseformula(formula):
    ch_queue = Queue()
    for character in formula:
        ch_queue.enqueue(character)
    if ch_queue.peek() is not None:
        readmolecule(ch_queue)


def readmolecule(ch_queue):
    # Första saken i molekylen måste vara en grupp
    readgroup(ch_queue)
    # Kolla om molekylen är färdig
    # Om molekylen inte är färdig, fortsätt med nästa grupp
    # readmolecule(whatsleft)


# Gruppen måste börja med "(" eller stor bokstav
def readgroup(ch_queue):
    if ch_queue.peek().isalpha():
        if ch_queue.peek().islower():
            raise ParseError("Saknad stor bokstav vid radslutet")
    elif ch_queue.peek() == "(":

            '''
            index = molecule.index(")")
            # Mol i parentes
            parmol = molecule[1:index]
            num = molecule[index + 1]
            # Kollar att det är en siffra och att det är ett positivt heltal
            readnum(num)
            try:
                num = int(num)
                if num < 2:
                    raise ValueError
            except ValueError:
                raise ParseError("Saknad siffra vid radslutet", )'''

    '''elif molecule[0].islower():
        raise ParseError("Saknad stor bokstav vid radslutet")'''
    else:
        raise ParseError("Felaktig gruppstart vid radslutet")


def readatom():
    pass


def readletter():
    pass


def readnum():
    pass


def main():
    formula = input("Mata in en kemisk förening för syntaxanalys, eller # för att avsluta programmet: \n")
    if formula != "#":
        parseformula(formula)


    '''while True:
        molecule = input("")
        if molecule == "#":
            break
        formula_queue.enqueue(molecule)
    print(formula_queue)
    readformulas(formula_queue)'''


# Startar programmet om programmet startar i denna fil. (Startar ej programmet ifall det kallas från en annan fil)
# (Behövs egentligen inte här)
if __name__ == "__main__":
    main()
