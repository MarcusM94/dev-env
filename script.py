import sys


def main():
    output = sys.stdin.read().split()
    for word in output:
        if word.upper() == 'FAILED':
            sys.exit(0)
    sys.exit(1)
        


if __name__ == '__main__':
    main()
