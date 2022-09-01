# coding: utf-8
from docopt import docopt
from modele import getenrs, rawstr2enr

from to import chi2cons
from to import cons2chi
from to import alphabet_prime
from to import getMotPrime
from to import getCode
import pickle
quels_nombres = dict()


# je veux une structure de données qui
# pour un nombre donné associe des numeros de ligne du dico
# Fi: nb -> seq< l1, l2...>
# seq< <nb, fi(nb)> >

from modele import rawstr2enr, getpho, pho2nb, pho2red

usage = """Usage: batch.py creedicobinaire"""
def makeDicoBinaire():
    with open("Dico332KmotsUTF8.txt", 'r') as fcsv:
        for num_ligne, ligne in enumerate(fcsv):
            enrs = getenrs(rawstr2enr(ligne.rstrip("\n")))
            if len(enrs['phored']) > 0:
                if enrs['code'] not in quels_nombres.keys():
                    quels_nombres[enrs['code']] = list()
                quels_nombres[enrs['code']].append(enrs)

    pickle.dump(quels_nombres, open("save.p", "wb"))
    print((sorted(list(quels_nombres.keys()))))

def main():
    makeDicoBinaire()

if __name__ == '__main__':
    args = docopt(usage)
    if args['creedicobinaire']:
        main()











