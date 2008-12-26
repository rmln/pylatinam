"""Verbs

Verbs
=====

About
-----

This module deals with Latin conjugation (inflexion of the verbs). The
idea is that user/program passes to the module verb forms and, if 
all functions well the module will return Latin tenses, moods, asp
ects and participles.

Class and functions
-------------------

The module contains several funcions and a single class. This class is
called Ver() and it is a wrapper around numerous functions. The
functions are not methods of the class since once functions are ca-
lled, the is no need for them any longer - outputs are attributes of
the class Ver(). If needed, functions can be wrapped and used outside
class calls.

Affixes
-------

Affixes in creating verb inflexions are suffixes and infixes. Suffixes
are passed from Str().VerStr() instance, while infixes are created and
passes inside the appropriate functions.

Keys
----

Each verb inflexion has a unique key, and these are stored in vkyes dict-
ionary. You can see it by reading __doc__ of conjugation() or run:

>>> print tags()

to get a table.

Examples
--------

>>> verb = Ver("specto")
>>> verb.entry
['specto', 'spectare', '1', 'spectavi', 'spectatum']
>>> a["ipra"]
['spectao', 'spectas', 'spectat', 'spectamus', 'spectatis', 'spectaunt']
>>> a.tenses

(...)
(lists all created items)

TODO: Thing that needs urgent
attention is present base, which is
invalid for verbs like fugio or lego.
This means that make_presentBase MUST
be written to support these verbs and
all inflexions that use present base must
be updated.

* changelog

+ present for 4
+ present base for -io, -uo
- present for 3, 1


"""


__version__="0.2.3.4"
__author__= "mlinar"
__mail__ = "cheesepy [a] gmail.com"


# Import exception relevant to this
# module only:

from pylatinam.pylatexcept import \
     InvalidParticipleEntryError, \
     InvalidInfinitiveEndingError, \
     InvalidInfinitiveID, \
     TenseNotDefinedError

from morphout import Show
from strings import VerStr, vkeys
from irregaux import *
from pylatinam.lexicon.lexicon import LexContainer

Suf = VerStr()
Esse = Esse()


def tags():
    """Compiles strings for tense IDs (auxiliary function)

    Usage in console:

    >>> print tags()
    
    """
    tag = ""
    tag += "Supported inflexions and appropriate keys\n\n"
    for item in vkeys.keys():
        tag += ("%s\t - %s\n" %(item.ljust(10,' '), vkeys[item]))
    return tag


class Ver:
    """Creates dictionary with Latin tenses.
    """

    __name__ = "Ver"

    def __init__(self, vword, pos="v", mode="words", nolex=False):
        "init"
        container = LexContainer(vword, pos="v", nolex=nolex, mode=mode)
        self.entry = container.entry
        self.word = container.word
        self.pos = container.pos
        self.translate = container.translate
        self.nolex = nolex
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
        
        present_base = make_presentBase(verb, conj_id)   #make present base, need full verb!
        perfect_base = make_perfectBase(verb)               #make perfect base
        present_ending = verb[0][-2:]                       #make present ending
        participle_base = participle_form(part)             #make participle base
        infinitive = verb[1]
        self.tenses = conjugation(conj_id, present_base, \
                     perfect_base, present_ending, \
                        participle_base, infinitive)                    #make available tenses
        self.participle = participles(participle_base)      #make available participles
        #morph attribute:
        self.morph = {"present_base":present_base, "perfect_base":perfect_base,
                      "present_ending":present_ending, "participle_base":participle_base,
                      "infinitive":infinitive}

    def __getitem__(self, key):
        try:
            return self.tenses[key]
        except KeyError:
            raise TenseNotDefinedError("That tense is not defined")

    def ident(self, form):
        """Identify form of the verb.
        Searches tenses only for time being.
        """
        for tense in self.tenses.keys().sort():
            i = 0
            for person in self.tenses[tense]:
                if person == form:
                    print vkeys[tense], tense, i
                i+=1

    def show(self, detail=None):
        "show conjugation"
        Show(self)


def conjugation(conj_id, present_base, perfect_base, present_ending, participle_base, infinitive):
    """Make conjugation dictionary --> .tense in Ver().
    
    Conjugation function
    ====================
    
    Conjugation dictionary created in this function is the
    attribute Ver().tense. Each tense has unique key in
    dictionary.

    In order to make temporal inflexions, this function does
    the following:

     - checks if infinitive ends in are/ere/ire
     - creates present base
     - creates perfect base
     - calls tense function

    Switches for calling tense lists
    --------------------------------

    ID, tense and participle::
    
        iplperp   	 - Indicative imperfect passive
        ind_p_fu  	 - Indicative Passive Future
        sub_a_pl  	 - Subjunctive Active Pluperfect
        sub_a_pe  	 - Subjunctive Active Perfect
        imp_p_fu  	 - Imperative Passive Future
        inf_a_pr  	 - The present active infinitive
        iperp     	 - Indicative perfect passive
        inf_a_pe  	 - The perfect active infinitive
        par_a_fu  	 - The future active participle
        sub_a_pr  	 - Subjunctive Active Present
        imp_a_fu  	 - Imperative Active Future
        ind_a_pr  	 - Indicative Active Present
        ind_p_im  	 - Indicative Passive Imperfect
        ind_p_pl  	 - Indicative Passive Pluperfect
        ind_a_pe  	 - Indicative Active Perfect
        inf_p_fu  	 - The future passive infinitive
        ind_a_pl  	 - Indicative Active Pluperfect
        sum_p_im  	 - Subjunctive Passive Imperfect
        imp_p_pr  	 - Imperative Passive Present
        gev       	 - The gerundive
        inf_a_fu  	 - The future active infinitive
        par_a_pr  	 - The present active participle
        imp_a_pr  	 - Imperative Active Present
        ind_p_pr  	 - Indicative Passive Present
        ged       	 - The gerund
        ind_p_pe  	 - Indicative Passive Perfect
        ind_a_im  	 - Indicative Active Imperfect
        sub_p_pr  	 - Subjunctive Passive Present
        par_p_pr  	 - The perfect passive participle
        ind_a_fu  	 - Indicative Active Future
        ind_a_fp  	 - Indicative Active Future Perfect
        inf_p_pe  	 - The perfect passive infinitive
        sub_a_im  	 - Subjunctive Active Imperfect
        ind_p_fp  	 - Indicative Passive Future Perfect
        supn      	 - The supine
        sub_p_pe  	 - Subjunctive Passive Perfect
        inf_p_pr  	 - The present passive infinitive
        sub_p_pl  	 - Subjunctive Passive Pluperfect

    Example:

    >>> Ver("certo").tense["ind_a_pr"]

    will list present forms of verb "compete".

    """
    
    tense = {}
    #Tenses, aspects and moods in Latin:
    tense["ind_a_pr"] = conj_ind_a_pr(conj_id, present_base)
    tense["ind_a_im"] = conj_ind_a_im(conj_id, present_base)
    tense["ind_a_fu"] = conj_ind_a_fu(conj_id, present_base)
    tense["ind_a_pe"] = conj_ind_a_pe(conj_id, perfect_base)
    tense["ind_a_pl"] = conj_ind_a_pl(conj_id, perfect_base)
    tense["ind_a_fp"] = conj_ind_a_fp(conj_id, perfect_base)
    tense["imp_a_pr"] = conj_imp_a_pr(conj_id, present_base)
    tense["imp_p_pr"] = conj_imp_p_pr(conj_id, infinitive, present_base) # c
    tense["imp_p_fu"] = conj_imp_p_fu(conj_id, present_base)
    tense["imp_a_fu"] = conj_imp_a_fu(conj_id, present_base)
    tense["ind_p_pr"] = conj_ind_p_pr(conj_id, present_base, present_ending)
    tense["ind_p_im"] = conj_ind_p_im(conj_id, present_base)
    tense["ind_p_fu"] = conj_ind_p_fu(conj_id, present_base, present_ending)
    tense["sub_a_pr"] = conj_sub_a_pr(conj_id, present_base)
    tense["sub_p_pr"] = conj_sub_p_pr(conj_id, present_base)
    tense["sub_a_im"] = conj_sub_a_im(infinitive)
    tense["sub_p_im"] = conj_sub_p_im(infinitive)
    tense["sub_a_pe"] = conj_sub_a_pe(perfect_base)
    tense["sub_a_pl"] = conj_sub_a_pl(perfect_base)
    
    #TODO: Put the above in dictionary as objects?
    #
    tense["ind_p_pe"] = (Esse.ipra, participle_parpp(participle_base))
    tense["ind_p_pl"] = (Esse.iima, participle_parpp(participle_base))
    tense["sub_p_pe"] = (Esse.sub_pr, participle_parpp(participle_base))
    tense["sub_p_pl"] = (Esse.sub_im, participle_parpp(participle_base))
    tense["ind_p_fp"] = (Esse.ind_fu, participle_parpp(participle_base))
    
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
    """Makes regular perticiple."""
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

# Indicative Active Present ------------------------------------------
    
def conj_ind_a_pr(conj_id, present_base):
    """Indicative present active.

    Examples:
        1st: amo, amas, amat, amamus, amatis, amant
        2nd: timeo, times, timet, timemus, timetis, timent
        3rd: tollo, tollis, tollit, tollimus, tollitis, tolunt
        4th: aperio, aperis, aperit, aperimus, aperitis, aperunt
    
    """
    cv = []
    suf = Suf.indicative_present
    if conj_id == 3:
        infix = "i"
    elif conj_id == 1 or conj_id == 2 or conj_id == 4:
        infix = ""
    else:
        raise InvalidInfinitiveID

    for item in suf:
        s_present_base = present_base
        infix = "i"
        if conj_id == 1:
            infix = ""
            if item == "o":
                infix == ""
        if conj_id == 2:
            pass
        if conj_id == 3:
            if item == "o":
                infix = ""
            if s_present_base.endswith("i"):
                infix = ""
            if item == "nt":
                infix = "u"
            
        if conj_id == 4:
            if item == "nt":
                infix = "u"
            else:
                #No infix for verbs like aperio,ire,4 because
                #their stem is aperi-, that is, it already
                #has "i" vocal.
                infix = ""

        cv.append("%s%s%s" % (s_present_base, infix, item))
            
        
##        if (conj_id == 1 or conj_id == 3 or conj_id == 4) and item == "nt":
##            infix="u"
##        elif (conj_id == 1 or conj_id == 3) and item == "o":
##            infix = ""
##        #No infix for verbs like aperio,ire,4 because
##        #their stem is aperi-, that is, it already
##        #has "i" vocal.
##        elif conj_id == 4:
##            infix = ""
##        else:
##            infix = "i"
##
##        cv.append("%s%s%s" % (present_base, infix, item))

    #corrections:
    #Ie: laudo in 1sg.pr.ind. is laudo, not laudao
    if conj_id == 1:
        cv[0]= "%s%s" % (cv[0][:-2], "o")
    
    return cv

# Indicative Passive Present -----------------------------------------

def conj_ind_p_pr(conj_id, present_base, present_ending):
    """Indicative Passive Present"""
    cv = []
    suf = Suf.indicative_present_passive
    if conj_id == 1 or conj_id == 2:
        vocal = "","","","","",""
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

# Imperative Active Present ------------------------------------------

def conj_imp_a_pr(conj_id, present_base):
    """Imperative Active Present"""
    
    #This imperative (modus imperativus) has
    #two persons only: 2nd sg & pl
    #cv = [None,"",None,None,"",None]
    cv = ["","","","","",""]
    if conj_id == 1 or conj_id == 2 or conj_id == 4:
        cv[1]=present_base
        cv[4]=present_base + "te"
    elif conj_id == 3:
        cv[1]=present_base + "e"
        cv[4]=present_base + "ite" #is this ok? applies to all?
    else:
        raise InvalidInfinitiveID
    return cv


# Indicative Active Imperfect ----------------------------------------

def conj_ind_a_im(conj_id, present_base):
    """Indicative Active Imperfect"""
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

# Indicative Active Future -------------------------------------------

def conj_ind_a_fu(conj_id, present_base):
    """Indicative Active Future"""
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

# Indicative Active Perfect ------------------------------------------

def conj_ind_a_pe(conj_id, perfect_base):
    """Indicative Active Perfect"""
    cv = []
    for item in Suf.perfect:
        cv.append('%s%s' % (perfect_base, item))
    return cv

# Indicative Active Pluperfect ---------------------------------------

def conj_ind_a_pl(conj_id, perfect_base):
    """Indicative Active Pluperfect"""
    cv=[]
    for item in Suf.ind_act_pluperfect:
        cv.append("%s%s" % (perfect_base, item))
    return cv

# Indicative Active Future Perfect -----------------------------------

def conj_ind_a_fp(conj_id, perfect_base):
    """Indicative Active Future Perfect"""
    cv=[]
    for item in Suf.future2:
        cv.append("%s%s" % (perfect_base, item))
    return cv

# Imperative Passive Future ------------------------------------------

def conj_imp_p_fu(conj_id, present_base):
    """Imperative Passive Future"""
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
            cv.append("%s%s%s%s" % (present_base, vocal[i], suf[i], "r"))
    return cv

# Imperative Active Future ------------------------------------------

def conj_imp_a_fu(conj_id, present_base):
    """Imperative Passive Future"""
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

# Imperative Passive Present ------------------------------------------

def conj_imp_p_pr(conj_id, infinitive, present_base):
    """Imperative Passive Present"""
    cv = []
    # Present passive indicative form of the second person plural:
    suf = 'mini'
    cv = ["" for x in range(6)]
    cv[1] = infinitive
    if conj_id == 3:
        cv[4] = ("%s%s%s" % (present_base, "i", suf))
    else:
        cv[4] = ("%s%s" % (present_base, suf))
    return cv



# Indicative Passive Imperfect ---------------------------------------

def conj_ind_p_im(conj_id, perfect_base):
    """Indicative Passive Imperfect"""
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

# Indicative Passive Future ------------------------------------------

def conj_ind_p_fu(conj_id, present_base, present_ending):
    """Indicative Passive Future"""
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

# Subjunctive Active Present

def conj_sub_a_pr(conj_id, present_base):
    """Subjunctive act. present

    s - substracts from base s characters,
        this is later needed for theme vowel
    
    """
    cv = []
    suf = Suf.sub_a_pr
    s = -1
    if conj_id == 1:
        infix = "e"
    elif conj_id == 2:
        infix = "ea"
    elif conj_id == 3:
        infix = "a"
        s = None
    elif conj_id == 4:
        infix = "ia"
    
    for item in suf:
        cv.append("%s%s%s" % (present_base[:s], infix, item))

    return cv

# Subjunctive Passive Present

def conj_sub_p_pr(conj_id, present_base):
    """Subjunctive act. present"""
    cv = []
    s = -1
    suf = Suf.sub_p_pr
    if conj_id == 1:
        infix = "e"
    elif conj_id == 2:
        infix = "ea"
    elif conj_id == 3:
        infix = "a"
        s = None
    elif conj_id == 4:
        infix = "ia"
    
    for item in suf:
        cv.append("%s%s%s" % (present_base[:s], infix, item))

    return cv

# Subjunctive Active Imperfect

def conj_sub_a_im(infinitive):
    """Subjunctive Active Imperfect"""
    cv = []
    suf = Suf.sub_a_pr
    for item in suf:
        cv.append("%s%s" % (infinitive, item))
        
    return cv

# Subjunctive Passive Imperfect

def conj_sub_p_im(infinitive):
    """Subjunctive Passive Imperfect"""
    cv = []
    suf = Suf.sub_p_pr
    for item in suf:
        cv.append("%s%s" % (infinitive, item))
        
    return cv

# Subjunctive Active Perfect
# Great page for subjunctive:
#   http://www.slu.edu/colleges/AS/languages/classical/latin/tchmat/grammar/whprax/w-sbjctvs.html

def conj_sub_a_pe(perfect_stem):
    """Subjunctive Active Perfect"""
    cv = []
    suf = Suf.sub_a_pr
    for item in suf:
        cv.append("%s%s%s" % (perfect_stem, 'eri', item))
        
    return cv

# Subjunctive Active Pluperfect


def conj_sub_a_pl(perfect_stem):
    """Subjunctive Passive Perfect"""
    cv = []
    suf = Suf.sub_a_pr
    for item in suf:
        cv.append("%s%s%s" % (perfect_stem, 'isse', item))
        
    return cv



#
#
# Other
# 
#

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
    """Makes present verb base."""
    if conj_id == 3:
        # For verbs like cupio, statuo
        # the present base is cupi-, statu-
        if verb[0].endswith("io") or verb[0].endswith("uo"):
            b_present = verb[0][:-1]
        else:
            b_present = verb[1][:-3]
    elif conj_id == 4:
        b_present = verb[1][:-2] 
    else:    
        b_present = verb[1][:-2]
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
