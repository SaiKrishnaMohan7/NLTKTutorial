import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#Chunking - Grouping of things; Grams... ngrams?

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

            #print(tagged)

            chunkGram = r'''Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}'''

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print (chunked)
            
            #matplotlib required
            chunked.draw()
    except Exception as e:
        print(str(e))

process_content(tokenized)