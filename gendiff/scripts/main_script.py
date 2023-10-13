from gendiff.diff.gendiff import parser
from gendiff.diff.diff import generate_diff


def main():
    print(generate_diff(*parser()))


if __name__ == '__main__':
    main()
