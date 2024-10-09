"""
dictionary according to wikipedia with keys as latin alphabet and values as Morse Code, 
I plan to loop in the string and access each value building the resulting string on Morse Code
for simplicity only most used puntctuation have been included"""

morse_dict = { 
    'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-', ' ': '     ',
    ':':'---...'
}
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
