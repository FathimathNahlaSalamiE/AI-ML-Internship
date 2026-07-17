from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
print(stemmer.stem("playing"))
print(stemmer.stem("working"))
print(stemmer.stem("learning"))
print(stemmer.stem("running"))
