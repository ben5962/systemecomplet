# coding:utf-8

chi2cons = {
    "0": ["z","s"],
    "1": ["d", "t"],
    "2": ["n", "G"],
    "3": "m",
    "4": "r",
    "5": "l",
    "6": ["j", "H"],
    "7": ["k", "g"],
    "8": ["v", "f"],
    "9": ["b", "p"],
}

cons2chi = {
    'z': '0',
    's': '0',
    't': '1',
    'd': '1',
    'n': '2',
    'G': '2',
    'm': '3',
    'r': '4',
    'l': '5',
    'j': '6',
    'H': '6',
    'k': '7',
    'g': '7',
    'v': '8',
    'f': '8',
    'b': '9',
    'p': '9'
}


# soit A(lphabet)' l alphabet restreint aux lettres des clefs de cons2chi.
# soit mot' un mot restreint aux lettres de A'
# la plupart des mot' de MOTS' sera le mot-vide
# soit code' le nombre corresponsant à la series de lettres restantes
# si mot' non vide

alphabet_prime = list(cons2chi.keys())

def getMotPrime(motphonetique: str)->str:
    motprime = ""
    for lettre in motphonetique:
        if lettre in alphabet_prime:
            motprime += lettre
    return motprime


def getCode(motphonetique: str)->str:
    code = ""
    motprime = ""
    motprime = getMotPrime(motphonetique)
    for lettre in motprime:
        code += cons2chi[lettre]
    return code
