"""Error classes - pyLatinam package

Exceplion classes for pyLatinam.

"""

__version__="0.2.6"
__author__= "mlinar"
__url__ = "http://www.pylatinam.com/"

class Error(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, info=""):
        self.info = self.__doc__
##    def __str__(self):
##        return repr(self.info)

class DictionaryError(Error):
    """Dictionary not found."""

class GenderError(Error):
    """Wrong gender reference for given noun (exception maybe?)."""
    
class NoGenderError(Error):
    """Wrong gender reference (not f, m or n)."""
    
class NoStemError(Error):
    """No stem found for that prefix."""
    
class DictionaryFileOpenError(Error):
    """Problems with specified dictionary tag or file problem."""
    
class CannotSetDeclensionError(Error):
    """Program cannot decide which declension the word belongs to.
    Check nom., gen. and gender."""
    
class ItemNumberError(Error):
    """Item 'word' containing info (list) about the word is invalid
    because it contains wrong number of items."""

class WordListFormatError(Error):
    """3-item list must be input data."""

class NoWordInLexiconError(Error):
    """No word in lexicon"""

class UndefinedPOSError(Error):
    """Part of speech (pos) string not defined."""

class LexiconItemNotFoundError(Error):
    """Word not defined in lexicon file"""

class WrongInflectionTypeError(Error):
    """Inflection for word is not logical. For example,
    if verb in declension or conjuction to conjugation."""

class CannotSetConjError(Error):
    """Conjugation cannot be determined;
    2nd item in lis must contain -are/ere/ire"""

class InvalidParticipleEntryError(Error):
    """Wrong participle"""

class InvalidInfinitiveEndingError(Error):
    """Verb must have infinitive in -are or -ere or -ire"""

class InvalidInfinitiveID(Error):
    """Verb must have infinitive id 1,2,3 or 4."""

class NoPrepCongruIdError(Error):
    """Preposition class must have congruence id for cases."""

class TenseNotDefinedError(Error):
    """Tense is not defined for that id."""

class CannotFindBase(Error):
    """The program cannot find right base for the word and the
    declension"""

class BlendingError(Error):
    """The program cannot combine ie. nominative and genitive.
    Is this the Latin word?"""

#Lexicon
class LexModeError(Error):
    """Modes for lexicon search can only be: simple, full, fcont and idle."""


#Adjectives:

class InvalidGenitiveCompError(Error):
    """Genitive mus end in -i or -is."""

class InvalidComparationIDError(Error):
    """ID must be 'comp' for comparative and 'sup' for
    superlative."""

#Strings:

class WordLengthInsufficientError(Error):
    """Number of letters in not valid for other arguments."""

# General:

class YetToImplementError(Error):
    """The requested operation is yet to be implemented."""
