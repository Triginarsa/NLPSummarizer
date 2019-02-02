from api import Stemmer

PorterStemmer = Stemmer()
a = PorterStemmer.stem("added")
print(a)