"""Pronouns

Pronouns
========

It is possible to get pronouns in two ways, but in both quite a lot of
details is needed.

 1. The first way is built-in:

    >>> a = Pron()
    >>> a["per,2sg,2"]
    >>> 'tibi'
    >>> a["per,3sg,2,f"]
    >>> 'iis|eis'

    Note that pipe character (|) indicates alternative forms.

    Arguments for __getitem__ method must be in correct order
    specified as::

        pronoun type, person, case, gender

    Example:

    >>> a["per,2sg,2"]

    means:

    "Return second person singular of personal pronoun in
    dative."

    Or:

    >>> a["per,3sg,3,f"]

    "Return third person singular, feminine form, of personal
    pronoun in accusative."

    IMPORTANT: If you retrieve 3rd person pronoun you must specify
    gender, otherwise class will return masculine form.

    Note: You can provide arguments as iterable.

 2. The second way is an attribute:

    When you create instance you have at your disposal dictionaries
    with genders and classes of pronouns. Names of dictionaries are
    keys of __pron__ dictionary.

TODO
*Add rest of the pronouns
*Rewrite error routines in __getitem__
"""

__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"
__mail__ = "cheesepy [a] gmail.com"
__version__="0.2.1"


from noun import Nom

PERSONS = ["1sg","2sg","3sg","1pl","2pl","3pl"]
GENDERS = ["m","f","n"]

class Pron:
    """Predifined Latin pronouns
    
    """
    
    __name__ = "Pron"

    __pron__ = {"per": "Personal pronouns", "ref": "Reflexive pronouns",
                "poss": "Possessive pronouns", "pref": "Possessive reflexive pronouns"}
    
    def __init__(self):

        #part of speech id
        self.pos = "pron"

        #Personal
        _1sg = 'ego','mei','mihi','me',None,'(a)me|mecum'
        _2sg = 'tu','tui','tibi','te','tu','(abs)te|tecum'
        _1pl = 'nos','nostri|nostrum','nobis','nos','nos','(a)nobis|nobiscum'
        _2pl = 'vos','vestri|vestrum','vobis','vos','vos','(a)vobis|vobiscum'

        _3sg = {
            'm':('is','eius','ei','eum',None,'(ab)eo|(cum)eo'), \
            'f':('ea','eius','ei','eam',None,'(ab)ea|(cum)ea'), \
            'n':('id','eius','ei','id',None,'(ab)eo|(cum)eo')}

        _3pl = {
            'm':('ii','eorum','iis|eis','eos',None,'(ab)iis,eis|(cum)iis,eis'), \
            'f':('eae','earum','iis|eis','eas',None,'(ab)iis,eis|(cum)iis,eis'), \
            'n':('ea','eorum','iis|eis','ea',None,'(ab)iis,eis|(cum)iis,eis')}

        self.per = {"1sg":_1sg, "2sg":_2sg, "3sg":_3sg, \
                    "1pl":_1pl, "2pl":_2pl, "3sg":_3pl}

        #Reflexive
        _reflexive = (None, "sui", "sibi", "se", None, "(a)se|secum")
        self.ref = {"3sg":_reflexive, "3pl":_reflexive}

        #Possessive
        n = Nom
        _p1sg = {}
        _p1sg["m"] = n(['meus','i','m'], nolex=True).casii
        _p1sg["f"] = n(['mea','ae','f'], nolex=True).casii
        _p1sg["n"] = n(['meum','i','n'], nolex=True).casii
        _p2sg = {}
        _p2sg["m"] = n(['tuus','i','m'], nolex=True).casii
        _p2sg["f"] = n(['tua','ae','f'], nolex=True).casii
        _p2sg["n"] = n(['tuum','i','n'], nolex=True).casii
        _p1pl = {}
        _p1pl["m"] = n(['noster','nostri','m'], nolex=True).casii
        _p1pl["f"] = n(['nostra','ae','f'], nolex=True).casii
        _p1pl["n"] = n(['nostrum','i','n'], nolex=True).casii
        _p2pl = {}
        _p2pl["m"] = n(['vester','vestri','m'], nolex=True).casii
        _p2pl["f"] = n(['vestra','ae','f'], nolex=True).casii
        _p2pl["n"] = n(['vestrum','i','n'], nolex=True).casii
        _p = ["eius" for i in range(11)]
        _p3sg = {}
        _p3sg = {"m":_p,"f":_p,"n":_p}
        _p = ["earum|eorum" for i in range(11)]
        _p3pl = {}
        _p3pl = {"m":_p,"f":_p,"n":_p}

        self.poss = {"1sg":_p1sg, "2sg":_p2sg, "3sg":_p3sg, \
                    "1pl":_p1pl, "2pl":_p2pl, "3sg":_p3pl}

        #Possesive reflexive
        _pr3m = n(['suus','i','m'], nolex=True).casii
        _pr3f = n(['sua','ae','f'], nolex=True).casii
        _pr3n = n(['suum','i','n'], nolex=True).casii
        self.pref = {}
        self.pref = {"3sg": {"m":_pr3m, "f":_pr3f, "n":_pr3n},
                     "3pl": {"m":_pr3m, "f":_pr3f, "n":_pr3n}}


    def __getitem__(self, args):
        """Get the pronoun: type, person + s/p, case, gender
        """
        NARG = 4
        if type(args) == str:
            args = args.split(",")
        if len(args) != NARG:
            args = list(args)
            for i in range(NARG - len(args)):
                args.append(-1)
        #errors:
        if not ["per","ref","poss","pref"].__contains__(args[0]):
            raise "InvalidType"
        if args[0]=="per":
            if not PERSONS.__contains__(args[1]):
                raise "InvalidPerson"
            #TODO: Add warning for check bellow?
            if not GENDERS.__contains__(args[3]) and args[1][0] == "3":
                raise "InvalidGender"
        if args[0]=="ref" or args[0]=="pref":
            if not ["3sg","3pl"].__contains__(args[1]):
                raise "InvalidPerson - Reflexive pronoun has 3rd person only"
        if args[0]=="poss" or args[0]=="pref":
            if not GENDERS.__contains__(args[3]):
                raise "InvalidGender"
        if int(args[2]) > 5 or int(args[2]) < 0: raise "InvalidCase"
        #
        ptype  = args[0]
        per    = args[1]
        case   = int(args[2])
        gn     = args[3]
        #
        pronouns = getattr(self, ptype)
        if ptype == "per":   
            if per[0] != "3":
                return pronouns[per][case]
            else:
                return pronouns[per][gn][case]
        if ptype == "ref":
            return pronouns[per][case]
        if ptype == "poss" or ptype == "pref":
            return pronouns[per][gn][case]
        
