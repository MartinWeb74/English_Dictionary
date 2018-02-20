import json
from difflib import get_close_matches

# the json file contains key value pairs
# the variable 'data' will contain a Python dictionary with the key value pairs
data = json.load(open("data.json"))


# 'word' is the key to search for in the dictionary
def translate(word):
    word_lowercase = word.lower()
    if word in data: # check whatever the user typed first
        print_nice(data[word])
    elif word_lowercase in data: # then check all lowercase
        print_nice(data[word_lowercase])
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        match() # ask user and process new word
    else:
        print("Can't find that word, sorry.")



# find a close match
def match():
    close_match = get_close_matches(word, data.keys(), cutoff=0.8)[0]
    ask = input( "Did you mean %s instead? Y for yes, N for no: " % close_match )
    if ask.lower() == "y":
        print_nice(data[close_match])
    else:
        print("No match found")



# format the print output
def print_nice(w):
    if type(w) == list:
        for item in w:
            print("-" * len(item))
            print(item)
    else:
        print(w)


# ask user for a word, save it to 'word'
word = input("Word to search: ")

# run the program
translate(word)

