from __future__ import division
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk import word_tokenize

import numpy


import nltk
import math

# nltk.download('punkt')
# nltk.download('stopwords')

class NlpToolKit:
    identifier = "NlpToolKit Class"

    def __init__( self ):
        print "Instance of ", self.identifier , "created"

    #tokenize menggunakan lib
    def tokenize( self, source ):
        result = word_tokenize( source )

        return [ token.lower() for token in result if token.isalnum() ]

    #stemming menggunakan porter lib
    def stem( self, tokens ):
        stemmer = nltk.stem.PorterStemmer()

        return [stemmer.stem(token) for token in tokens]

    def stopwords_removal( self, words ):
        stops = set(stopwords.words('english'))
        return [word for word in words if word not in stops]


    def inverse_document_frequencies(self, tokenized_documents):
        idf_values = {}
        all_tokens_set = set([item for sublist in tokenized_documents for item in sublist])
        for tkn in all_tokens_set:
            contains_token = map(lambda doc: tkn in doc, tokenized_documents)
            idf_values[tkn] = 1 + math.log(len(tokenized_documents)/(sum(contains_token)))
        return idf_values

    def sublinear_term_frequency(self, term, tokenized_document):
        count = tokenized_document.count(term)
        if count == 0:
            return 0
        return count/len(tokenized_document)
        # return 1 + math.log(count)

    def cosine_similarity(self, vector1, vector2):
        dot_product = sum(p*q for p,q in zip(vector1, vector2))
        magnitude   = math.sqrt(sum([val**2 for val in vector1])) * math.sqrt(sum([val**2 for val in vector2]))
        if not magnitude:
            return 0
        return dot_product/magnitude