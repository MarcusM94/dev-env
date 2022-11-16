import sys


def main():
    output = sys.stdin.readlines()
    for line in output:
        for word in line:
            if word.upper() == 'FAILED':
                sys.exit(False)
    sys.exit(True)


if __name__ == '__main__':
    main()
