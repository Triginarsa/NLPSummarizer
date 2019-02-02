
from nltk.corpus import wordnet as wn
from nltk import word_tokenize

import nltk

class TextProcessor:
    identifier = "TextProcessor"
    
    def __init__( self ):
        print "Instance of ", self.identifier , "created"

    def splitParagraphs( self, document ):
        return document.split('\n')

    def splitSentences( self, document ):
        return document.split('. ')
