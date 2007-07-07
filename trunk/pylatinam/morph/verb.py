"""Verbs (package pyLatinam)

About

This module deals with Latin conjugation (inflexion of the verbs). The
idea is that user/program passes to the module verb forms and, if all
is functioninig well, the module would return Latin tenses, moods, asp
ects and participles.

Class and functions

The module contains several funcions and single class. This class is
called Ver() and serves as a wrapper around numerous funcions. The
functions are not attributes of the class since once functions are ca-
lled, the is no need to deal with them - outputs are attributes of
the class Ver(). If needed, functions can be wrapped and used outside
class calls.

Affixes

Affixes in creating verb inflexions are suffixes and infixes. Suffixes
are passed from Str().VerStr() instance, while infixes are created and
passes inside the apprioriate functions.

Keys

Each verb infexion has unique key, and these are stored in tkyes dict-
ionary. You can see it by reading __doc__ of conjugation() or run

>>> print tags()

to get a table.

Examples:

>>> verb = Ver("specto")
>>> verb.entry
['specto', 'spectare', '1', 'spectavi', 'spectatum']
>>> a["ipra"]
['spectao', 'spectas', 'spectat', 'spectamus', 'spectatis', 'spectaunt']
>>> a.tenses
(...)
(lists all created items)
"""

    #
    #NOTA BENE: Thing that needs urgent
    #attention is present base, which is
    #invalid for verbs like fugio or lego.
    #This means that make_presentBase MUST
    #be writen to supprt these verbs and
    #all inflexions that use present base must
    #be updated.
    #

__author__= "miller"
__mail__ = "cheesepy@gmail.com"
__version__="0.4.9"


# Import exception relevant to this
# module only:

from latinam.ltexcept import \
     InvalidParticipleEntryError, \
     InvalidInfinitiveEndingError, \
     InvalidInfinitiveID, \
     TenseNotDefinedError


from strings import VerStr
from irregaux import *
from latinam.lexicon.lexicon import Lex

Suf = VerStr()
Esse = Esse()

tkeys =  {'ipra':'Indicative present active', \
         'iima':'Indicative imperfect active', \
         'futa1':'Future active I', \
         'iper':'Indicative perfect active', \
         'iplu':'Indicative pluperfect active', \
         'futa2':'Indicative future I', \
         'imp1':'Indicative imperative I', \
         'imp2':'Indicative imperative II or Furure imperative',\
         'ipp':'Indicative present passive',\
         'iimperp':'Indicative imperfect passive',\
         'futp1': 'Future passive I', \
         'iperp': 'Indicative perfect passive',\
         'iplperp': 'Indicative imperfect passive' }

pkeys = {'parpp': 'Participle perfect passive'}

def tags():
    """Auxiliary function: compiles strings for tense IDs"""
    tag = ""
    tag += "Supported inflexions and appropriate keys\n\n"
    for item in tkeys.keys():
        tag += ("%s\t - %s\n" %(item.ljust(10,' '), tkeys[item]))
    return tag


class Ver:
    """Creates dictionary with Latin tenses.
    """

    def __init__(self, vword, nolex=False):
        self.nolex = nolex #does app use lexicon or not? default is False
        if nolex==False:
            lex = Lex(vword, pos="v") #current word
            self.entry = lex.entry #this is the word as defined in lex file
            self.translate = lex.lookup
        else: #applies if word is not looked up in lexicon file:
            self.entry = vword.split(",")
            self.lookup = []
            self.translate = []
        self.word = vword
        #
        verb = self.entry                                   #just a synonym
        conj_id = int(verb[2])                              #1,2,3 or 4
        check_infinitive(verb[1])
        #See if pariciple is provided. If not,
        #it is considered regular.
        try:
            part = verb[4]
        except:
            part = make_participle(verb[1])
        
        present_base = make_presentBase(verb[1], conj_id)   #make present base
        perfect_base = make_perfectBase(verb)               #make perfect base
        present_ending = verb[0][-2:]                       #make present ending
        participle_base = participle_form(part)             #make participle base
        self.tenses = conjugation(conj_id, present_base, \
                     perfect_base, present_ending, \
                        participle_base)                    #make available tenses
        self.participle = participles(participle_base)      #make available participles
        #morph attribute:
        self.morph = {"present_base":present_base, "perfect_base":perfect_base,
                      "present_ending":present_ending, "participle_base":participle_base}

    def __getitem__(self, key):
        try:
            return self.tenses[key]
        except KeyError:
            raise TenseNotDefinedError("That tense is not defined")

    def ident(self, form):
        """Identify form of the verb.
        Searches tenses only, for time being.
        """
        for tense in self.tenses.keys().sort():
            i = 0
            for person in self.tenses[tense]:
                if person == form:
                    print tkeys[tense], tense, i
                i+=1

    def show(self, detail=0):
        "show conjugation"
        v = self.entry
        t = self.translate
        print "\n", "VERB CONJUGATION", "\n", 70*"-"
        print "Verb:           ", v
        if len(t) and detail==1:
            print "Translation(s): ", [w[1] for w in t]
        print
        for item in tkeys.keys():            
            print "\t", tkeys[item], "\n"
            tmp = self.tenses[item]
            for i in tmp:
                print "\t", i
            print "\t", 66*"-"
        if detail==1:
            if self.nolex:
                print "Lexicon not used."
            else:
                print "Lexicon used."
            print "Module version", __version__

def conjugation(conj_id, present_base, perfect_base, present_ending, participle_base):
    """Make conjugation dictionary --> .tense in Ver().

    Conjugation dictionary created in this function is the
    attribute Ver().tense. Each tense has unique key in
    dictionary.

    In order to make temporal inflexions, this function does
    the following:

    -checks if infinitive ends in are/ere/ire
    -creates present base
    -creates perfect base
    -calls tense function

    Swithes for calling tense lists:

    imp2	 - Indicative imperative II or Furure imperative
    iplperp	 - Indicative imperfect passive
    imp1	 - Indicative imperative I
    ipp	         - Indicative present passive
    futp1	 - Future passive I
    futa2	 - Indicative future I
    futa1	 - Future active I
    iima	 - Indicative imperfect active
    iplu	 - Indicative pluperfect active
    iimperp	 - Indicative imperfect passive
    iper	 - Indicative perfect active
    iperp	 - Indicative perfect passive
    ipra	 - Indicative present active

    Example: Ver("certo").tense["ipra"] will list present
    forms of verb "compete".

    """
    
    tense = {}
    #Tenses, aspects and moods in Latin:
    tense["ipra"] = conj_ipra(conj_id, present_base)
    tense["iima"] = conj_iima(conj_id, present_base)
    tense["futa1"] = conj_futa1(conj_id, present_base)
    tense["iper"] = conj_iper(conj_id, perfect_base)
    tense["iplu"] = conj_iplu(conj_id, perfect_base)
    tense["futa2"] = conj_iplu(conj_id, perfect_base)
    tense["imp1"] = conj_imp1(conj_id, present_base)
    tense["imp2"] = conj_imp2(conj_id, present_base)
    tense["ipp"] = conj_ipp(conj_id, present_base, present_ending)
    tense["iimperp"] = conj_iimperp(conj_id, present_base)
    tense["futp1"] = conj_futp1(conj_id, present_base, present_ending)
    #
    tense["iperp"] = (participle_parpp(participle_base), Esse.ipra)
    tense["iplperp"] = (participle_parpp(participle_base), Esse.iima)
    return tense
        
def participle_form(participle):
    """Returns participle base --> Ver().participle_base
    This function is called from Ver() and then passed to
    participles().
    """
    participle_endings = Suf.participle_perfect_passive
    participle_valid = False
    for item in participle_endings:
        if participle.endswith(item):
            participle_valid = True
    if participle_valid:
        participle_form = participle[:-2]
        return participle_form
    else:
        raise InvalidParticipleEntryError

def make_participle(infinitive):
    """make regular perticiple"""
    return "%s%s" % (infinitive.strip("re"), "um")
    
def participles(participle_form):
    """Makes participles by calling participle functions.
    Note that participle_form is stem to which suffixes are
    added, and not full participle entry. This value is passed
    from function participle_form() which makes participle
    stem from full participle entry.
    """
    ptc = {}
    ptc['parpp']= participle_parpp(participle_form)
    return ptc

def participle_parpp(participle_form):
    """Participle perfect passive"""
    cv = []
    suf = Suf.participle_perfect_passive
    for item in suf:
        cv.append("%s%s" % (participle_form, item))
    return cv
    
    
def conj_ipra(conj_id, present_base):
    """Indicative present active."""
    cv = []
    suf = Suf.indicative_present
    if conj_id == 3:
        infix = "i"
    elif conj_id == 1 or conj_id == 2 or conj_id == 4:
        infix = ""
    else:
        raise InvalidInfinitiveID
    
    for item in suf:
        if (conj_id == 1 or conj_id == 3) and item=="nt":
            infix="u"
        if conj_id == 1 and item=="o":
            infix=""
            
        cv.append("%s%s%s" % (present_base, infix, item))

    #corrections:
    #Ie: laudo in 1sg.pr.ind. is laudo, not laudao
    if conj_id == 1:
        cv[0]= "%s%s" % (cv[0][:-2], "o")
    
    return cv

def conj_iima(conj_id, present_base):
    """Indicative imperfect active."""
    cv = []
    suf = Suf.indicative_present
    if conj_id == 1 or conj_id == 2:
        infix = "ba"
    elif conj_id == 3 or conj_id == 4:
        infix = "eba"
    else:
        raise InvalidInfinitiveID

    for item in suf:
        if item == "o": item = "m"
        cv.append("%s%s%s" % (present_base, infix, item))
        
    return cv

def conj_futa1(conj_id, present_base):
    """Future I active."""
    cv = []
    if conj_id == 1 or conj_id == 2:
        suf = Suf.future1n2
    elif conj_id == 3 or conj_id == 4:
        suf = Suf.future3n4
    else:
        raise InvalidInfinitiveID
    #add correction for vocal base
    for item in suf:
        if present_base.endswith("ue") and item=="ent":
            item="eent"
        cv.append("%s%s" % (present_base, item))
    
    return cv

def conj_iper(conj_id, perfect_base):
    """Perfect active."""
    cv = []
    for item in Suf.perfect:
        cv.append('%s%s' % (perfect_base, item))
    return cv

def conj_iplu(conj_id, perfect_base):
    """Pluperfect active."""
    cv=[]
    for item in Suf.ind_act_pluperfect:
        cv.append("%s%s" % (perfect_base, item))
    return cv

def conj_futa2(conj_id, perfect_base):
    """Future II."""
    cv=[]
    for item in Suf.futa2:
        cv.append("%s%s" % (perfect_base, item))
    return cv

def conj_imp1(conj_id, present_base):
    """Imperative present."""
    
    #This imperative (modus imperativus) has
    #two persons only: 2nd sg & pl
    cv = [None,"",None,None,"",None]
    if conj_id == 1 or conj_id == 2 or conj_id == 4:
        cv[1]=present_base
        cv[4]=present_base + "te"
    elif conj_id == 3:
        cv[1]=present_base + "e"
        cv[4]=present_base + "ite" #is this ok? applies to all?
    else:
        raise InvalidInfinitiveID
    return cv

def conj_imp2(conj_id, present_base):
    """Imperative II or Imperative furure"""
    cv = []
    suf = Suf.imperative_future
    #This needs more work :(
    if conj_id == 1 or conj_id == 2 or conj_id == 4:
        vocal = "","","","","",""
    elif conj_id == 3:
        vocal = "","i","i","","i","u"
    else:
        raise InvalidInfinitiveID

    for i in range(6):
        if suf[i] == None:
            cv.append(None)
        else:
            cv.append("%s%s%s" % (present_base, vocal[i], suf[i]))
    return cv

def conj_ipp(conj_id, present_base, present_ending):
    """Indicative present passive"""
    cv = []
    suf = Suf.indicative_present_passive
    if conj_id == 1 or conj_id == 2:
        vocal = "","o","","","",""
    elif conj_id ==3:
        if present_ending == "io":
            vocal = "i","e","i","i","i","u"
        else:
            vocal = "","e","i","i","i","u"
    elif conj_id == 4:
        vocal = "","","","","","u"
    else:
        raise InvalidInfinitiveID

    for i in range(6):
        cv.append("%s%s%s" % (present_base, vocal[i], suf[i]))
    #correction
    if conj_id == 1:
        cv[0]=cv[0][:-3]+"or"
    return cv

def conj_iimperp(conj_id, perfect_base):
    """Indicative imperfect passive."""
    cv = []
    suf = Suf.indicative_imperfect_passive
    if conj_id == 1 or conj_id == 2:
        vocal = ""
    elif conj_id == 3 or conj_id == 4:
        vocal = "e"
    else:
        raise InvalidInfinitiveID
    
    for item in suf:
        cv.append('%s%s%s' % (perfect_base, vocal, item))
    return cv

def conj_futp1(conj_id, present_base, present_ending):
    """Future passive I"""
    cv = []
    if conj_id == 1 or conj_id == 2:
        suf = Suf.future1_passive1n2
    elif conj_id == 3 or conj_id == 4:
        suf = Suf.future1_passive3n4
        if conj_id == 3 and present_ending == "io":
            present_base = present_base + "i"
    else:
        raise InvalidInfinitiveID
    for item in suf:
        cv.append("%s%s" % (present_base, item))
    return cv
        

def make_perfectBase(verb, full=False):
    """Make perfect verb base."""
    # The following code could be more
    # straightforward, but is left for
    # easier upgrades.
    try:
        perfect = verb[3]
    except IndexError:
        #If there is no perfect form, it is
        #assumed that is regular:
        perfect = verb[1][:-2] + "vi"
    else:
        if not perfect.endswith("i"):
            # It is possible that function passes
            # wrong form of infinitive (if it is not provided
            # in dictionary), which means that verb probably
            # has regular perfect. The following code will
            # make regular form.
            perfect = lex_verb[1][:-2] + "vi"

    if full==False:
        return perfect[:-1]

def make_presentBase(verb, conj_id):
    """Make present verb base."""
    if conj_id == 3:
        b_present = verb[:-3]
    else:    
        b_present = verb[:-2]
    return b_present

def check_infinitive(infinitive):
    """Check if infinitive is valid."""
    infinitive_endings = Suf.infinitive_endings
    infinitive_checked = False
    for item in infinitive_endings:
        if infinitive.endswith(item):
            infinitive_checked = True
    if infinitive_checked == False:
        raise InvalidInfinitiveEndingError
