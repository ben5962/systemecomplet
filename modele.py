# coding: utf-8
from docopt import docopt

# je veux une methode qui me permette d acceder à un enregistrement donné
# par son numero d index

from to import getCode
from to import getMotPrime


def getrawenr(num_enr: int)->str:
    nom_fichier = "Dico332KmotsUTF8.txt"
    with open(nom_fichier) as f:
        for numero,contenu in enumerate(f):
            if num_enr == numero:
                return contenu.rstrip("\n")




usage = """Usage: modele.py --getenr=<numenr> [--getpho] [--getnb] [--getphored]
"""



def getenr(num_enr: int)->list:
    return rawstr2enr(getrawenr(num_enr))

def rawstr2enr(rawenr:str)->str:
    return rawenr.split(";")

def getpho(enr:list)->str:
    numero_champ_pho = 1
    return enr[numero_champ_pho]


# je veux une methode qui me donne le nb que
# cette mnemonique ourrait rappeler
def pho2nb(pho:str)->str:
    return getCode(pho)


# je veux une methode qui me donne la ch phonétique reconnue
def pho2red(pho:str)->str:
    return getMotPrime(pho)


# je veux une methode qui me permette d acceder à la partie
# mot  d un enregistrement

def getmot(enr: list)->str:
    index_mot = 0
    return enr[index_mot]



# je veux une methode qui, depuis un enregistrement
# me donne un enregistement structuré: une sequence
# de clefs valeurs telles que:
# 'code' -> pho2nb()
# 'contenu' -> getmot()
# 'phonetique' -> getpho()
# 'phored' -> pho2red()
def getenrs(enr=None)->dict:
    enrs = dict()
    enrs['code'] = pho2nb(getpho(enr))
    enrs['contenu'] = getmot(enr)
    enrs['phonetique'] = getpho(enr)
    enrs['phored'] = pho2red(getpho(enr))
    return enrs


def test_getenrs():
    enr =  ["encharbonnerez,encharbonnerai", "AHarbOneré", "3"]
    valeur_obtenue = getenrs(enr)
    valeur_attendue = { 
        'code': '64924',
        'contenu' : "encharbonnerez,encharbonnerai",
        'phonetique' : "AHarbOneré",
        'phored': 'Hrbnr'
    }
    assert valeur_obtenue == valeur_attendue


# je veux une methode qui me permette d acceder à la partie
# mot  d un enregistrement
def test_getmot():
    enr = ["encharbonnerez,encharbonnerai", "AHarbOneré", "3"]
    valeur_attendue = "encharbonnerez,encharbonnerai"
    valeur_obtenue = getmot(enr)
    assert valeur_attendue == valeur_obtenue



def test_pho2red():
    pho = "AHarbOneré"
    valeur_attendue = pho2red(pho)
    valeur_obtenue = "Hrbnr"
    assert valeur_attendue == valeur_obtenue


def test_rawstr2enr():
    rawenr = getrawenr(125)
    valeur_obtenue = getenr(125)
    valeur_attendue = ["encharbonnerez,encharbonnerai", "AHarbOneré", "3"]
    assert valeur_obtenue == valeur_attendue

def test_getpho():
    enr = getenr(125)
    valeur_obtenue = getpho(enr)
    valeur_attendue = "AHarbOneré"
    assert valeur_obtenue == valeur_attendue


def test_pho2nb():
    pho = "AHarbOneré"
    valeur_attendue = "64924"
    valeur_obtenue = pho2nb(pho)
    assert valeur_attendue == valeur_obtenue

def test_getenr():
    valeur_obtenue = getrawenr(125)
    valeur_attendue = "encharbonnerez,encharbonnerai;AHarbOneré;3"
    assert valeur_obtenue == valeur_attendue

def main(num_enr:int, pho=False, nb=False, phored=False):
    enr = getenr(num_enr)
    chaine = str(enr)
    if pho:
        chaine += " " + getpho(enr)
    if nb:
        chaine += " " + pho2nb(getpho(enr))
    if phored:
        chaine += " " + pho2red(getpho(enr))
    print(chaine)





if __name__ == '__main__':
    args = docopt(usage)
    if args['--getenr']:
        numero_enr = int(args['--getenr'])
        main(numero_enr, args['--getpho'],
             args['--getnb'], args['--getphored'])
