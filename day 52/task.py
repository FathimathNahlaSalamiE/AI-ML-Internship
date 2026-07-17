sentence_1 = 'I love Machine Learning'
sentence_1 = sentence_1.split()
print(sentence_1)

sentence_2 = 'HELLO WORLD'
sentence_2 = sentence_2.lower()
print(sentence_2)

import re
sentence_3 = 'Python!!! is Awesome???'
sentence_3 = re.sub(r'[^a-zA-Z\s]','',sentence_3)
print(sentence_3)

sentence_4 = 'The cat is sitting on the chair'
sentence_4 = sentence_4.lower()
sentence_4 = sentence_4.split()
stop_words = ['the','is','on']
result = [word for word in sentence_4 if word not in stop_words]
print(result)

sentence_5 = 'AI 2025 is AMAZING!!!       '
sentence_5 = sentence_5.lower()
sentence_5 = re.sub(r'[^a-zA-Z\s]','',sentence_5)
sentence_5 = sentence_5.split()
stop_words = ['the','is','on']
result = [word for word in sentence_5 if word not in stop_words]
print(result)