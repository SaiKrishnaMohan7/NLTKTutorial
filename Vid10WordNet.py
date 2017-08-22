from nltk.corpus import wordnet

'''
synonyms = wordnet.synsets('program')

#Prints a list of synonyms of the parameters
print(synonyms)

#Prints list Lemmatized versions of the synonyms
print('Lemmatized---->', synonyms[0].lemmas())

#Prints just the name ?
print(synonyms[0].name())

#definitions
print('definition of the first element --->' ,synonyms[0].definition())

#Examples of usage of a word;returns a list
print(synonyms[0].examples())
'''

'''
synonyms = []
antonyms = []

rootWordSyns = wordnet.synsets('good')

for synonym in rootWordSyns:
    for lemmatizedWord in synonym.lemmas():
        #Appending the root of all the synonyms
        synonyms.append(lemmatizedWord.name())
        #check for antonyms
        if lemmatizedWord.antonyms():
            antonyms.append(lemmatizedWord.antonyms()[0].name())

print(set(synonyms))

print(set(antonyms))
'''
'''Similarity'''
#Naming convention word.noun.posInTheList
word_1 = wordnet.synset('ship.n.01')
word_2 = wordnet.synset('boat.n.01')

print(word_1.wup_similarity(word_2))#0.9090909090909091 similar!