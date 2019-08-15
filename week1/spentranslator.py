# Created and done by Alexander Mitchell
# This program is a dictionary for translating English to Spanish words so my lazy friend Ted can do his homework

# 1. Create a list of English words and their Spanish equivalents
entospwords = {'hello': 'hola', 'this': 'eso', 'computer science': 'ciencias de la computacion',
               'is': 'es', 'hello this is computer science': 'hola eso es ciencias de la computacion', 
               'nah don\'t worry':'na no te preocupes', 
               'I like horses':'me gusta caballos', 'hamburgers are delicious': 'hamburguesas son deliciosas'}
spntoenwords = {'hola': 'hello', 'eso': 'this', 'ciencias de la computacion': 'computer science',
                'es': 'is', 'hola eso es ciencias de la computacion': 'hello this is computer science',
                'na no te preocupes': 'nah don\'t worry', 
                'me gusta caballos': 'I like horses', 'hamburguesas son deliciosas': 'hamburgers are delicious'}

# Get the desired word to translate from the user
word = raw_input("What do you want to translate, Ted: ").lower()
# print(word)

# Since he is looking up one off words, he would put one word in and try to see if there is a match
if word in entospwords.keys():
    print(entospwords[word])
elif word in spntoenwords.keys():
    print(spntoenwords[word])
else:
    print("Lo siento, Ted.")
