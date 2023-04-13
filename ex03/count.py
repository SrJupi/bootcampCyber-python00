import sys
import string

def text_analyzer(text=None):
    '''This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.'''
    if text == None:
        text = input("What is the text to analyze?\n>> ")
    try:
        assert isinstance(text, str), "argument is not a string"
    except AssertionError as msg:
        print("AssertionError:", msg)
    else:
        uppers = 0
        lowers = 0
        punctuations = 0
        spaces = 0
        for letter in text:
            if letter.isupper():
                uppers += 1
            elif letter.islower():
                lowers += 1
            elif letter.isspace():
                spaces += 1
            elif letter in string.punctuation:
                punctuations += 1
        print(f'''The text contains {len(text)} character(s):
- {uppers} upper letter(s)
- {lowers} lower letter(s)
- {punctuations} punctuation mark(s)
- {spaces} space(s)''')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("ERROR!\nUsage: python count.py STRING")
    else:
        text_analyzer(sys.argv[1])
