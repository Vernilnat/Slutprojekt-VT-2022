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
        self.par_count = 0

    def __str__(self):
        formula = ""
        current = self.first
        try:
            while current is not None:
                formula += current.value
                current = current.next
        except AttributeError:              # Fångar felet att current.next inte existerar än pga. att det
            pass                            # inte är definierat som en Node ännu
        return formula

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

    def isempty(self):
        if self.first is None:
            return True
        return False

    def peek(self):
        return self.first.value

    def par_tracker(self):
        return self.par_count


# Grundämnen
ATOMS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
         'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y',
         'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La',
         'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re',
         'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np',
         'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg',
         'Cn', 'Fl', 'Lv']


def parseformula(formula):
    ch_queue = Queue()
    try:
        for character in formula:
            ch_queue.enqueue(character)
        if ch_queue.isempty() is False:
            readmolecule(ch_queue)
        else:
            raise ParseError("Empty whaaat?")
        return "Formeln är syntaktiskt korrekt"
    except ParseError as e:
        return str(e) + str(ch_queue)


# <mol>   ::= <group> | <group><mol>
def readmolecule(ch_queue):
    # Första saken i molekylen måste vara en grupp
    readgroup(ch_queue)
    # Kolla om molekylen är färdig
    if ch_queue.isempty() is False:
        if ch_queue.peek() == ")":
            if ch_queue.par_count < 1:
                raise ParseError("Felaktig gruppstart vid radslutet ")
            return
        readmolecule(ch_queue)


# <group> ::= <atom> |<atom><num> | (<mol>) <num>
def readgroup(ch_queue):
    if ch_queue.peek().isalpha():
        readatom(ch_queue)
        if ch_queue.isempty() is False:
            if ch_queue.peek().isdigit():
                readnum(ch_queue)
    elif ch_queue.peek() == "(":
        ch_queue.get()
        ch_queue.par_count += 1
        readmolecule(ch_queue)
        if ch_queue.isempty() is False:
            if ch_queue.peek() == ")":
                ch_queue.get()
                ch_queue.par_count -= 1
                readnum(ch_queue)
        else:
            raise ParseError("Saknad högerparentes vid radslutet ")
    else:
        raise ParseError("Felaktig gruppstart vid radslutet ")


# Kallas från grupp
# <atom>  ::= <LETTER> | <LETTER><letter>
def readatom(ch_queue):
    if ch_queue.peek().isupper():
        atom = ch_queue.get()
        if ch_queue.isempty() is False:
            if ch_queue.peek().islower():
                atom = atom + ch_queue.get()
        if atom in ATOMS:
            return
        else:
            raise ParseError("Okänd atom vid radslutet ")
    else:
        raise ParseError("Saknad stor bokstav vid radslutet ")


def readnum(ch_queue):
    if ch_queue.isempty() is True:
        raise ParseError("Saknad siffra vid radslutet ")

    num = ch_queue.get()
    if num.isdigit() is False:
        raise ParseError("Saknad siffra vid radslutet ")
    if num == "0":
        raise ParseError("För litet tal vid radslutet ")
    while True:
        if ch_queue.first is None:
            break
        if ch_queue.peek().isdigit():
            num += ch_queue.get()
        else:
            break
    if int(num) > 1:
        return
    else:
        raise ParseError("För litet tal vid radslutet ")


def main():
    print("Mata in en kemisk förening för syntaxanalys, eller # för att avsluta programmet:")
    while True:
        formula = input()
        if formula == "#":
            quit()
        else:
            result = parseformula(formula)
            print(result)


# Startar programmet om programmet startar i denna fil. (Startar ej programmet ifall det kallas från en annan fil)
# (Behövs egentligen inte här)
if __name__ == "__main__":
    main()
