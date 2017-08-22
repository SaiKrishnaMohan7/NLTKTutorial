"""This Module is just for fun"""
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Creating an instance of the Python Stemmer Class
porter_stemmer = PorterStemmer()

#Creating a set of Stop Words available by default
stop_words = set(stopwords.words('english'))

example_words = ['printer', 'printed', 'conker', 'conked', 'divided']

#Stemming example
for word in example_words:
    print(porter_stemmer.stem(word))


example_sentence = 'Its a beautiful day to Python. Pythoning seems like a good idea. In my mind I am pythonly. I do python with the python'

#Tokenizing the sentence
tokenized_sentence = word_tokenize(example_sentence)
print('Non tokenized sentence------>', example_sentence)
print('Tokenized sentence----->', tokenized_sentence)

filtered_sentence = []

#Filtering the tokenized sentence i.e. removing the articles
for word in tokenized_sentence:
    if word not in stop_words:
        filtered_sentence.append(word)

print('filtered sentence---->', filtered_sentence)

#Stemming each word in the filtered list
for word in filtered_sentence:
        print('Stem of the filtered word------->', porter_stemmer.stem(word))