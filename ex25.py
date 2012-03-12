# EC1
# Line 23-24
# The print_first_word function takes a list as an argument,
# pops the first word off it and stores it in a 'word' variable,
# then prints the contents of the variable.
# Since Python arguments are passed by reference, sorted_words
# now contains all the words of the sentence except the first
# word.
#
# Line 25-26
# print_last_word operates in the same way as print_first_word
# except it pops and prints the last word in a sentence
# instead of the first.
# 
# Line 27-28
# Typing sorted_words into the Python shell (is that the real
# name of it?) just prints the variable's value.  In this case
# we see the sorted_word list is missing its first and last word
# due to the print_first_word and print_last_word functions.
# 
# Line 29-31
# Assigns sorted_words to return the value of sort_sentence()
# which sorts the resulting list from break_words().
# The value of sorted_words is then displayed.
# 
# Line 32-24
# print_first_and_list calls break_words to split() the string 
# in sentence into a list of words.  This list is passed into 
# print_first_word and print_last_word.
# 
# Line 35-37
# print_first_and_last_sorted calls sort_sentence which results
# in a list of sorted words from the sentence string.  The word
# list is then passed into print_first_word and print_last_word.
# 
# Line 38
# Control-D to exit the shell.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
