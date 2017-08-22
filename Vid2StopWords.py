from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is And example blah. And yet the fox is blah and the greeen shrek of pink blue cheese"

#ALl the stopwords will be a set predefined english words
#Can be modified to include my set of stop words as well
stop_words = set(stopwords.words("english"))

#print(stop_words)

#Tokenizing the sentence, returns a list
words = word_tokenize(example_sentence)
print('before filtering, tokenized------>', words)

#initilaizing an empty list
filtered_sentence = []

#the segment below can be replaced with
#filtered_sentence = [word for word in words if not word in stop_words]
print(filtered_sentence)

#looping through the tokenized words
for word in words:
    #checking if each word a part of the stop words
    if word not in stop_words:
        #if not a part of stop words then it is good and can be considered to be filtered
        filtered_sentence.append(word)

print('after filtering, tokenized------>', filtered_sentence)

#if 'and' is capitalized as And, they are not filtered 