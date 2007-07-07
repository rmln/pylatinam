"""Import namespaces

Import this file with * argument to get most often used
functions and classes form the whole package.

Nom()       - noun declension
Adj()       - adjectival declension
Ver()       - conjuction of verbs
Pronoun()   - pronouns
Conj(), Intj(), Adv() - stem classes only


"""
#constants:

V = 'v'
N = 'n'
ADJ = 'adj'
P = 'prep'
C = 'conj'
I = 'int'
ADV = 'adv'

#classes:

from latinam.morph.noun import Nom
from latinam.morph.verb import Ver
from latinam.morph.pronoun import Pron
from latinam.morph.cai import Conj, Intj, Adv
from latinam.morph.adjective import Adj, Adjf

##from latinam.morph.irregaux import *
##from latinam.lexicon.lexicon import *
##from latinam.sintax.sentence import *
##from latinam.morph.strings import *
