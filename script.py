import sys


def main():
    output = sys.stdin.read()
    print(output)
    for word in output.split():
        if word.upper() == 'FAILED':
            sys.exit(1)
    sys.exit(0)
        


if __name__ == '__main__':
    main()
