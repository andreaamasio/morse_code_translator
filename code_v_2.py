import pandas as pd

# Load the Morse code table from Wikipedia
link = "https://en.wikipedia.org/wiki/Morse_code"

# build df with pandas
df = pd.read_html(link)[0]

#extracting only letters and numbers (until 36 index), after they are not parsed correctly and mess with the dictionary
keys=[character[0] for character in df.Character[:36]]
codes=[cod[:-1].replace("▄▄▄","-").replace("▄",".").replace("\xa0","")  for cod in df.Code[:36]]

morse_dict=dict(zip(keys,codes))


#result:
""" {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 
'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', 
'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}
"""
# missing characters to append not parsed
additional_morse = {
    ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '     ',
    ':': '---...'
}

# Using .update() to append additional_morse to morse_dict
morse_dict.update(additional_morse)



#now the dictionary is like the ones we had in version 1
# # morse_dict = { 
#     'A':'.-', 'B':'-...',
#     'C':'-.-.', 'D':'-..', 'E':'.',
#     'F':'..-.', 'G':'--.', 'H':'....',
#     'I':'..', 'J':'.---', 'K':'-.-',
#     'L':'.-..', 'M':'--', 'N':'-.',
#     'O':'---', 'P':'.--.', 'Q':'--.-',
#     'R':'.-.', 'S':'...', 'T':'-',
#     'U':'..-', 'V':'...-', 'W':'.--',
#     'X':'-..-', 'Y':'-.--', 'Z':'--..',
#     '1':'.----', '2':'..---', '3':'...--',
#     '4':'....-', '5':'.....', '6':'-....',
#     '7':'--...', '8':'---..', '9':'----.',
#     '0':'-----', ', ':'--..--', '.':'.-.-.-',
#     '?':'..--..', '/':'-..-.', '-':'-....-',
#     '(':'-.--.', ')':'-.--.-', ' ': '     ',
#     ':':'---...'
# }
#I can finalize as version 1 now that I have dictionary:
#below find the main function used to build the string
def converter(text):
    to_print=""
    for letter in string:
        to_print+=morse_dict[letter.capitalize()] + ' '
    return to_print

#below we gather the input from the user
string=input("Write something to be converted in Morse Code: ")

#below we print the output in Morse Code
result=converter(string)
print(result)

