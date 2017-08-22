from nltk import sent_tokenize, word_tokenize

example_text = "Hello there, how are you? blah blah. humbum. glum glum."

#Tokenizes (groups by) by sentences and returns a list of sentences
print(sent_tokenize(example_text))

#Tokenizes (groups by) by sentences and returns a list of words
##Recognizes Punctuation, splits by punctuation. Mr. Sai will be split ['Mr.', 'Sai']
print(word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)