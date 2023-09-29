import argparse

from gendiff import generate_diff


prog = 'gendiff'
usage = 'usage: gendiff [options] <filepath1> <filepath2>'
description = 'Compares two configuration files and shows a difference.'


def main():
    parser = argparse.ArgumentParser(description, usage)
    parser.add_argument('file_1')
    parser.add_argument('file_2')
    parser.add_argument('-V', '--version',
                        help='output the version number',
                        action='store_true')
    parser.add_argument('-f', '--format', default='gendiff/files/',
                        help='output format (default: "stylish")',
                        action='store_true')
    args = parser.parse_args()
    print(generate_diff(args.file_1, args.file_2, args.format))


if __name__ == '__main__':
    main()
