#pylint: disable=C0103
'''Classifying a movie review based'''
import string
from itertools import chain

from nltk.corpus import movie_reviews as mr
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
import nltk
import pickle

'''Resources- https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict'''

#pickle is the way of saving Python objects
#here we are saving our trained classifier
stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

word_features = FreqDist(chain(*[i for i,j in documents]))
word_features = list(word_features.keys())[:100]

numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[numtrain:]]

classifier = nbc.train(train_set)
print((nltk.classify.accuracy(classifier, test_set)))
classifier.show_most_informative_features(5)

'''@params
        nameOfFileSavingTo, operation
        wb---> writeBytes'''
save_classifier = open('naivebayes.pickle', 'wb')
pickle.dump(classifier, save_classifier)
save_classifier.close()