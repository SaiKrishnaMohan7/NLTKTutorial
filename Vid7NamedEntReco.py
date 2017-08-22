import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import numpy

#Named Entity Recognition

'''training text for the PunktSentenceTokenizer, gives us a customized tokenize
    This can be used to train over own tokenizer
'''
train_text = state_union.raw('2005-GWBush.txt')
example_text = state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

#Tokenizing by sentence
tokenized = custom_sent_tokenizer.tokenize(example_text)
#print('Tokenizing by sentence--------->', tokenized)

#Function tokenizes every element in tokenized by word and then tags it
def process_content(tokenized_by_sentence):
    try:
        for i in tokenized_by_sentence:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            #namedEnt = nltk.ne_chunk(tagged)
            namedEnt = nltk.ne_chunk(tagged, binary=True)
            namedEnt.draw()
    
    except Exception as e:
        print(str(e))

process_content(tokenized)

'''
WHEN binary=False
NE Type and Examples
ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''