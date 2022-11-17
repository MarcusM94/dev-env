import sys


def main():
    output = sys.stdin.readlines().split()
    for word in output:
        print(word)


if __name__ == '__main__':
    main()
