import nltk

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("playing"))
print( lemmatizer.lemmatize("playing",pos="v" ))
print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("mice"))
print(lemmatizer.lemmatize("children"))


stemmer = PorterStemmer()
print(stemmer.stem("playing"))
print(stemmer.stem("working"))
print(stemmer.stem("learning"))
print(stemmer.stem("running"))
