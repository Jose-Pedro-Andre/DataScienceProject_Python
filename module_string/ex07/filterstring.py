
import sys

def main():
    n_args = len(sys.argv)

    if (n_args != 3): print("AssertionError: the arguments are bad"); sys.exit()
    try:
        int(sys.argv[2])
    except:
        print("AssertionError: the arguments are bad"); sys.exit()
    words = sys.argv[1].split(' ')
    size = int(sys.argv[2]);
    new_list = [i for i in words if (lambda x: len(x) > size)(i)]
    print(new_list)
main()

