#pylint: disable=C0103
'''Classifying a movie review based'''
import string
from itertools import chain
from statistics import mode

import nltk
from nltk.corpus import movie_reviews as mr
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import LinearSVC, NuSVC
from nltk.classify import ClassifierI


class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers
    
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
            return mode(votes)
    
    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

stop = stopwords.words('english')
documents = [([w for w in mr.words(i) if w.lower() not in stop and w.lower() not in string.punctuation], i.split('/')[0]) for i in mr.fileids()]

word_features = FreqDist(chain(*[i for i,j in documents]))
word_features = list(word_features.keys())[:3000]

numtrain = int(len(documents) * 90 / 100)
train_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[:numtrain]]
test_set = [({i:(i in tokens) for i in word_features}, tag) for tokens,tag in documents[numtrain:]]

classifier = nbc.train(train_set)
print((nltk.classify.accuracy(classifier, test_set)))
classifier.show_most_informative_features(5)

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train_set)
print('MNB CLassifeir accuracy: ', (nltk.classify.accuracy(MNB_classifier, test_set)))


BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(train_set)
print('BNB classifier accuracy', (nltk.classify.accuracy(BNB_classifier, test_set)))

LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(train_set)
print('LR Classifier accuracy', (nltk.classify.accuracy(LR_classifier, test_set)))

SGD_classifier = SklearnClassifier(SGDClassifier())
SGD_classifier.train(train_set)
print('SGD Classifier accuracy', (nltk.classify.accuracy(SGD_classifier, test_set)))

LSV_classifier = SklearnClassifier(LinearSVC())
LSV_classifier.train(train_set)
print('LSV Classifier accuracy', (nltk.classify.accuracy(LSV_classifier, test_set)))

NuSV_classifier = SklearnClassifier(NuSVC())
NuSV_classifier.train(train_set)
print('NuSV Classifier accuracy', (nltk.classify.accuracy(NuSV_classifier, test_set)))

voted_classifier = VoteClassifier(classifier, MNB_classifier, BNB_classifier, LR_classifier,
    SGD_classifier, LSV_classifier, NuSV_classifier)

print('voted_classifier accuracy', (nltk.classify.accuracy(voted_classifier, test_set)))

print('Classification:', voted_classifier.classify(test_set[0][0]), 'Confidence: ',
    voted_classifier.confidence(test_set[0][0]))

print('Classification:', voted_classifier.classify(test_set[0][0]), 'Confidence: ',
    voted_classifier.confidence(test_set[1][0]))

print('Classification:', voted_classifier.classify(test_set[0][0]), 'Confidence: ',
    voted_classifier.confidence(test_set[2][0]))

print('Classification:', voted_classifier.classify(test_set[0][0]), 'Confidence: ',
    voted_classifier.confidence(test_set[3][0]))