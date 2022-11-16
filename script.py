import sys


def main():
    output = sys.stdin.readlines()
    for line in output:
        print(line)
    for line in output:
        for word in line:
            if word.upper() == 'FAILED':
                sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
