#write a function for unique words. count the number of distinct words in a sentence.
sentence = "The cat and the hat"
def unique_words(sentence):
    words = sentence.lower().split()
    unique = set(words)
    print(len(unique))
unique_words(sentence)    