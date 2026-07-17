from nltk.stem import WordNetLemmatizer,PorterStemmer

lemmatizer = WordNetLemmatizer()
print("lemmatized")

words = [
    "cars",
    "running",
    "children",
    "mice",
    "studies",
    "playing",
    "studying",
    "hiding",
    "bathing",
    "sleeping"
]

for word in words:
    print(
        lemmatizer.lemmatize(word,pos="v")
    )

print()

stemmer = PorterStemmer()
print("stemmed")
for word in words:
    print(
        stemmer.stem(word)
    )