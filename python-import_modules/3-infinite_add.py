import sys

if __name__ == "__main__":
    argv = sys.argv[1:]

    for argument in argv:
        result = sum(int(argument))
        print(result)
