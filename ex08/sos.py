import sys

def morse_code_it(text):
    morse_dict = {'A':'.-', 'B':'-...',
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
                    '0':'-----', ' ':'/'}
    print(text)
    text = [morse_dict[letter.upper()] for letter in text]
    print(" ". join(text))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sos.py <STRING1> [STRING2...]")
    text = " ".join(sys.argv[1:])
    for letter in text:
        if not letter.isalnum() and not letter.isspace():
            print("Error: string must contain only alphanumeric and space")
            exit()
    morse_code_it(text)
