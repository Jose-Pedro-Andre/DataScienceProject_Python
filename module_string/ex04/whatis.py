import sys

def main():
    argc = sys.argv
    n_args = len(argc)
    if (n_args > 2 or n_args < 2):
        print("AssertionError: more than one argument is provided")
        return ;
    i = 0
    while( i < n_args):
        if (argc[1][i].isdigit() is False):
            print("AssertionError: argument is not an integer")
            return ;
        i += 1;
    num = int(argc[1])
    if (num < 0):
        num *= -1;
    if num % 2 == 0 :
        print("I'm Odd.")
    else:
        print("I'm Even.")
main()
        

