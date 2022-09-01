# coding: utf-8
import pickle
import docopt
from to import chi2cons
quels_nombres = dict()
quels_nombres = pickle.load(open("save.p", "rb"))


nom_fichier_phonetique = "Dico332KmotsUTF8.txt"



def estNombrePresent(nombre: str):
    return nombre in list(quels_nombres.keys())

def afficher_possibilites(nombre: str):
    if estNombrePresent(nombre):
        print("voici les possibilites")
        for idx, valeur in enumerate(quels_nombres[nombre]):
            print(str(idx), " ", print(str(valeur)))
    else:
        print("aucune possibilite avec: ", nombre)

# je veux une fonction qui,
# si je lui fournis la structure nb, [ lignes corresp ],

usage = """
Usage:
nombre.py <nb>
"""
def comment_memoriser(valeur: int):
    """interface cli .
    renvoie une serie de chaines contenant les mnemoniques possibles
    d un nb donné"""

    print("___" * 10)
    afficher_possibilites(valeur)


if __name__ == '__main__':

    args = docopt.docopt(usage)
    if args['<nb>']:
        nb_a_encoder = args['<nb>']
        comment_memoriser(nb_a_encoder)


