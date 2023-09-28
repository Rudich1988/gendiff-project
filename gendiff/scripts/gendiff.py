import argparse

from gendiff import generate_diff


prog = 'gendiff'
usage = 'usage: gendiff [options] <filepath1> <filepath2>'
description = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(prog, usage, description)
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    parser.add_argument('-V', '--version', help='output the version number')
    parser.add_argument('-f', '--format',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    print(generate_diff(args.file_1, args.file_2))


if __name__ == '__main__':
    main()
