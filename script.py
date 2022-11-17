import sys


def main():
    output = sys.stdin.read().split()
    for word in output:
        if word.upper() == 'FAILED':
            sys.exit(1)
    sys.exit(0)
        


if __name__ == '__main__':
    main()
