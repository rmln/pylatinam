"""Error classes - pyLatinam package

Exceplion classes for pypyLatinam.

"""

__version__="0.2.6"

class Error(Exception):
    """Base class for exceptions in this module."""

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
    """Werb must have infinitive in -are or -ere or -ire"""

class InvalidInfinitiveID(Error):
    """Werb must have infinitive id 1,2,3 or 4."""

class NoPrepCongruIdError(Error):
    """Preposition class must have congruence id for cases."""

class TenseNotDefinedError(Error):
    """Tense is not defined for that id."""

#Adjectives:

class InvalidGenitiveCompError(Error):
    """Genitive mus end in -i or -is."""

class InvalidComparationIDError(Error):
    """ID must be 'comp' for comparative and 'sup' for
    superlative."""
