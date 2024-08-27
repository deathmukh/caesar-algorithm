import string

def caesar(text,shift,alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
    shift_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shift_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

plain_text = "this is a test! Hhehe"
print(caesar(plain_text, 7,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))