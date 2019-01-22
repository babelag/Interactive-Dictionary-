import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yesorno = input(f"Did you mean {get_close_matches(word, data.keys())[0]} instead. Enter Y if yes, N if not?")
        if yesorno == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yesorno == "N":
            return "The word doesn't exist, try again"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist, try again"

word = input("Enter the word : ")

output = (translate(word))

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)