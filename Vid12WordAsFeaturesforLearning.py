import nltk
import random
from nltk.corpus import movie_reviews

#https://stackoverflow.com/questions/21107075/classification-using-movie-review-corpus-in-nltk-python

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

#print(documents[1])

all_words = [w.lower() for w in movie_reviews.words()]

#print(all_words)

all_words_freq_dist = nltk.FreqDist(all_words)

#print(all_words_freq_dist.most_common(15))

#print(all_words_freq_dist['silly']) #152

word_features = list(all_words.ketys())[:3000]