import nltk

nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("playing"))
print( lemmatizer.lemmatize("playing",pos="v" ))
print(lemmatizer.lemmatize("cars"))
print(lemmatizer.lemmatize("mice"))
print(lemmatizer.lemmatize("children")) 