from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize('cats'))

#singular is Baterium
print(lemmatizer.lemmatize('bacteria'))

print(lemmatizer.lemmatize('Coronations'))

#Gives adjective of the word, Default=noun
print(lemmatizer.lemmatize('better', pos='a'))

#Thinks better is the verb form of better
#Which implies that better doesn't have a verb
print(lemmatizer.lemmatize('better', pos='v'))


#The wordnet lemmatizer only knows four parts of speech (ADJ, ADV, NOUN, and VERB)