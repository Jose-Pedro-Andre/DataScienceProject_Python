
import sys

def filter(it, type):
    if (type == "digits"): return it.isnumeric()
    if type == "upper" : return it.isupper()
    if type == "lower" : return it.islower()
    if type == "space" : return it == ' ' 
    if type == "point" : return it in ",.!?:"
    return False
    
def ft_count_characters(sentences, type) -> int :
    iter = 0;
    for i in sentences:
        if (filter(i, type)):
            iter +=1
    return iter;


def main():
    sentence = sys.argv[1]
    print(f"The text contains {len(sentence)} charaters: ")
    print(f"{ft_count_characters(sentence, 'upper')} upper letters")
    print(f"{ft_count_characters(sentence, 'lower')} lower letters")
    print(f"{ft_count_characters(sentence, 'point')} puntuation marks")
    print(f"{ft_count_characters(sentence, 'space')} spaces")
    print(f"{ft_count_characters(sentence, 'digits')} digits")

main()