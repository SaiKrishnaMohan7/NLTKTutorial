from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw('bible-kjv.txt')

sent_tok = sent_tokenize(sample)

print(sent_tok)
