import sys

def code_morse(chr):
    morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/ '}
    if (morse_code.get(chr) is None): print("AssertionError: the arguments are bad"); sys.exit(1)
    return (morse_code[chr])
def main():
    n_args = len(sys.argv)
    new_sentences = ""
    if(n_args < 2 or n_args > 2): return ;
    sentence = sys.argv[1]
    for i in sentence :
        new_sentences += code_morse((i.upper()))
    print(new_sentences)
main()